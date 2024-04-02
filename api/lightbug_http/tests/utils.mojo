from python import Python, PythonObject
from lightbug_http.io.bytes import Bytes
from lightbug_http.error import ErrorHandler
from lightbug_http.uri import URI
from lightbug_http.http import HTTPRequest, HTTPResponse, ResponseHeader
from lightbug_http.net import Listener, Addr, Connection, TCPAddr
from lightbug_http.service import HTTPService, OK
from lightbug_http.server import ServerTrait
from lightbug_http.client import Client


alias default_server_host = "localhost"
alias default_server_port = 8080
alias default_server_conn_string = "http://" + default_server_host + ":" + default_server_port.__str__()

alias getRequest = String(
    "GET /foobar?baz HTTP/1.1\r\nHost: google.com\r\nUser-Agent: aaa/bbb/ccc/ddd/eee"
    " Firefox Chrome MSIE Opera\r\n"
    + "Referer: http://example.com/aaa?bbb=ccc\r\nCookie: foo=bar; baz=baraz;"
    " aa=aakslsdweriwereowriewroire\r\n\r\n"
)._buffer

alias defaultExpectedGetResponse = String(
    "HTTP/1.1 200 OK\r\nServer: M\r\nDate: Content-Length: 13\r\n\r\nHello world!"
)


@parameter
fn new_httpx_client() -> PythonObject:
    try:
        var httpx = Python.import_module("httpx")
        return httpx
    except e:
        print("Could not set up httpx client: " + e.__str__())
        return None


fn new_fake_listener(request_count: Int, request: Bytes) -> FakeListener:
    return FakeListener(request_count, request)


struct ReqInfo:
    var full_uri: URI
    var host: String
    var is_tls: Bool

    fn __init__(inout self, full_uri: URI, host: String, is_tls: Bool):
        self.full_uri = full_uri
        self.host = host
        self.is_tls = is_tls


struct FakeClient(Client):
    """FakeClient doesn't actually send any requests, but it extracts useful information from the input.
    """

    var name: String
    var host: StringLiteral
    var port: Int
    var req_full_uri: URI
    var req_host: String
    var req_is_tls: Bool

    fn __init__(inout self) raises:
        self.host = "127.0.0.1"
        self.port = 8888
        self.name = "lightbug_http_fake_client"
        self.req_full_uri = URI("")
        self.req_host = ""
        self.req_is_tls = False

    fn __init__(inout self, host: StringLiteral, port: Int) raises:
        self.host = host
        self.port = port
        self.name = "lightbug_http_fake_client"
        self.req_full_uri = URI("")
        self.req_host = ""
        self.req_is_tls = False

    fn do(self, req: HTTPRequest) raises -> HTTPResponse:
        return OK(String(defaultExpectedGetResponse)._buffer)

    fn extract(inout self, req: HTTPRequest) raises -> ReqInfo:
        var full_uri = req.uri()
        try:
            _ = full_uri.parse()
        except e:
            print("error parsing uri: " + e.__str__())

        self.req_full_uri = full_uri

        var host = String(full_uri.host())

        if host == "":
            raise Error("URI host is nil")

        self.req_host = host

        var is_tls = full_uri.is_https()
        self.req_is_tls = is_tls

        return ReqInfo(full_uri, host, is_tls)


struct FakeServer(ServerTrait):
    var __listener: FakeListener
    var __handler: FakeResponder

    fn __init__(inout self, listener: FakeListener, handler: FakeResponder):
        self.__listener = listener
        self.__handler = handler

    fn __init__(
        inout self, addr: String, service: HTTPService, error_handler: ErrorHandler
    ):
        try:
            self.__listener = FakeListener()
        except e:
            print(e)
        self.__handler = FakeResponder()

    fn get_concurrency(self) -> Int:
        return 1

    fn listen_and_serve(self, address: String, handler: HTTPService) raises -> None:
        ...

    fn serve(inout self) -> None:
        while not self.__listener.closed:
            try:
                _ = self.__listener.accept[FakeConnection]()
            except e:
                print(e)

    fn serve(self, ln: Listener, handler: HTTPService) raises -> None:
        ...


@value
struct FakeResponder(HTTPService):
    fn func(self, req: HTTPRequest) raises -> HTTPResponse:
        var method = String(req.header.method())
        if method != "GET":
            raise Error("Did not expect a non-GET request! Got: " + method)
        return OK(String("Hello, world!")._buffer)


@value
struct FakeConnection(Connection):
    fn __init__(inout self, laddr: String, raddr: String) raises:
        ...

    fn __init__(inout self, laddr: TCPAddr, raddr: TCPAddr) raises:
        ...

    fn read(self, inout buf: Bytes) raises -> Int:
        return 0

    fn write(self, buf: Bytes) raises -> Int:
        return 0

    fn close(self) raises:
        ...

    fn local_addr(inout self) raises -> TCPAddr:
        return TCPAddr()

    fn remote_addr(self) raises -> TCPAddr:
        return TCPAddr()


@value
struct FakeListener:
    var request_count: Int
    var request: Bytes
    var closed: Bool

    fn __init__(inout self) raises:
        self.request_count = 0
        self.request = Bytes()
        self.closed = False

    fn __init__(inout self, addr: TCPAddr) raises:
        self.request_count = 0
        self.request = Bytes()
        self.closed = False

    fn __init__(inout self, request_count: Int, request: Bytes) -> None:
        self.request_count = request_count
        self.request = request
        self.closed = False

    @always_inline
    fn accept[T: Connection](self) raises -> T:
        return FakeConnection()

    fn close(self) raises:
        pass

    fn addr(self) -> TCPAddr:
        return TCPAddr()


@value
struct TestStruct:
    var a: String
    var b: String
    var c: Bytes
    var d: Int
    var e: TestStructNested

    fn __init__(inout self, a: String, b: String) -> None:
        self.a = a
        self.b = b
        self.c = String("c")._buffer
        self.d = 1
        self.e = TestStructNested("a", 1)

    fn set_a_direct(inout self, a: String) -> Self:
        self.a = a
        return self

    fn set_a_copy(self, a: String) -> Self:
        return Self(a, self.b)


@value
struct TestStructNested:
    var a: String
    var b: Int

    fn __init__(inout self, a: String, b: Int) -> None:
        self.a = a
        self.b = b

    fn set_a_direct(inout self, a: String) -> Self:
        self.a = a
        return self

    fn set_a_copy(self, a: String) -> Self:
        return Self(a, self.b)

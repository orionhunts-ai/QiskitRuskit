from portkey_ai import Portkey

client = Portkey(
  api_key="V4NjnMLB1RiAPGFOvZu0KDAOZYU=",  # defaults to os.environ.get("PORTKEY_API_KEY")
)

# Make the prompt creation call with the variables
prompt_completion = client.prompts.completions.create(
  prompt_id="pp-chief-scie-cf44b1",
  variables={"goal":"","experimental_data":"","assessment":"","Goal":"","experimental data":""}
)

# Make the prompt creation call with the variables - stream mode
stream_prompt_completion = client.prompts.completions.create(
  prompt_id="pp-chief-scie-cf44b1",
  variables={"goal":"","experimental_data":"","assessment":"","Goal":"","experimental data":""},
  stream=True
)
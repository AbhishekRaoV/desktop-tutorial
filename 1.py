KeyError: 'predictions'
Traceback:
File "/home/ubuntu/.local/lib/python3.8/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 534, in _run_script
    exec(code, module.__dict__)
File "/home/ubuntu/abhi/evaluation/streamlit.py", line 67, in <module>
    response = get_bot_response(user_input)
File "/home/ubuntu/.local/lib/python3.8/site-packages/streamlit/runtime/legacy_caching/caching.py", line 716, in wrapped_func
    return get_or_create_cached_value()
File "/home/ubuntu/.local/lib/python3.8/site-packages/streamlit/runtime/legacy_caching/caching.py", line 697, in get_or_create_cached_value
    return_value = non_optional_func(*args, **kwargs)
File "/home/ubuntu/abhi/evaluation/streamlit.py", line 49, in get_bot_response
    bot_reply = output["predictions"][0]["candidates"][0]["content"]

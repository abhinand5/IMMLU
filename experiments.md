# Experiments in Generating Multiple Choice Questions (MCQs) in Indian Languates

## Experiment 1: Prompting ChatGPT in English to MCQs in Indian Languages
* Using [ChatGPT](https://chat.openai.com/), we prompted in English to generate MCQ's by topic (Science, Social Science, History, and Literature) for two different languates: Hindi and Malayalam.
    * [Chat History for Hindi](https://chat.openai.com/share/55149e7e-0588-474e-a59e-44e08b6583ca)
    * [Chat History for Malayalam](https://chat.openai.com/share/f04d0506-70f3-44e4-a067-2ee1b9cb04a7)
* We used human labelers to upvote / downvote the question / answer combination.
* The resulting data is in [chatgpt_samples.csv](data/chatgpt_samples.csv)


## Experiment 2: Translating the MMLU Dataset Using the Google Translation API

You can find an example in the [google_translate_api_examples](notebooks/google_translate_api_examples.ipynb) notebook. Due to our familiarity with the Tamil language, we translated the MMLU dataset to Tamil in batches of 100. The resultant data is in numbered CSV files in the [data folder](data/)

## Experiment 3: Using a Streamlit app to show question, answer, combination in a translated language to get approval

This section is WIP.
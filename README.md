# AGIEval
This repository contains information about AGIEval, data, code and output of baseline systems for the benchmark.

# Introduction
AGIEval is a human-centric benchmark specifically designed to evaluate the general abilities of foundation models in tasks pertinent to human cognition and problem-solving. 
This benchmark is derived from 20 official, public, and high-standard admission and qualification exams intended for general human test-takers, such as general college admission tests (e.g., Chinese College Entrance Exam (Gaokao) and American SAT), law school admission tests, math competitions, lawyer qualification tests, and national civil service exams. 
For a full description of the benchmark, please refer to our paper: [AGIEval: A Human-Centric Benchmark for
Evaluating Foundation Models](https://arxiv.org/pdf/2304.06364.pdf).

# Tasks and Data
[We have updated the dataset to version 1.1.](data/v1_1) The new version updated Chinese Gaokao (chemistry, biology, physics) datasets with questions from 2023 and addressed annotation issues. To facilitate evaluation, now all multi-choice question (MCQ) tasks have one answer only (Gaokao-Physics and JEC-QA used to have multi-label answers). AGIEval-en datasets remain the same as Verison 1.0. The new version's statistics are as follows:

AGIEval v1.1 contains 20 tasks, including 18 MCQ tasks and two cloze tasks (Gaokao-Math-Cloze and MATH). You can find the full list of tasks in the table below.
![The datasets used in AGIEVal](AGIEval_tasks.png)

You can download all post-processed data in the [data/v1_1](data/v1_1) folder. All usage of the data should follow the license of the original datasets. 

The data format for all datasets is as follows:
```
{
    "passage": null,
    "question": "设集合 $A=\\{x \\mid x \\geq 1\\}, B=\\{x \\mid-1<x<2\\}$, 则 $A \\cap B=$ ($\\quad$)\\\\\n",
    "options": ["(A)$\\{x \\mid x>-1\\}$", 
        "(B)$\\{x \\mid x \\geq 1\\}$", 
        "(C)$\\{x \\mid-1<x<1\\}$", 
        "(D)$\\{x \\mid 1 \\leq x<2\\}$"
        ],
    "label": "D",
    "answer": null
}
```
The `passage` field is available for gaokao-chinese, gaokao-english, both of logiqa, all of LSAT, and SAT. The answer for multi-choice tasks is saved in the `label` field. The answer for cloze tasks is saved in the `answer` field. 

We provide the prompts for few-shot learning in the [data/few_shot_prompts](data/few_shot_prompts.csv) file.
# Baseline Systems
We evaluate the performance of the baseline systems (gpt-3.5-turbo and GPT-4o) on AGIEval v1.1.
The results are as follows:

![The datasets used in AGIEVal](gpt_results.png)

You can replicate the results by following the steps below:
1. Update your OpenAI API in the [openai_api.py](openai_api.py) file.
2. run the [run_prediction.py](run_prediction.py) script to get the results.

# Evaluation
You can run the [post_process_and_evaluation.py](post_process_and_evaluation.py) file to get the evaluation results.
# Leaderboard
We report the leaderboard on AGIEval v1.1. The leaderboard contains two subsets AGIEval-en and AGIEval-zh. The two subset leaderboards contain only MCQ tasks. The leaderboard is as follows:

## AGIEval-en few-shot

| Model            | Source                                                   | Average |
|------------------|----------------------------------------------------------|---------|
| GPT-4o           | [Link](https://github.com/ruixiangcui/AGIEval)           | 71.4    |
| Llama 3 400B+    | [Link](https://ai.meta.com/blog/meta-llama-3/)           | 69.9    |
| Llama 3 70B      | [Link](https://ai.meta.com/blog/meta-llama-3/)           | 63      |
| Mixtral 8x22B    | [Link](https://ai.meta.com/blog/meta-llama-3/)           | 61.2    |
| GPT-3.5-Turbo    | [Link](https://github.com/ruixiangcui/AGIEval)           | 52.7    |
| Llama 3 8B       | [Link](https://ai.meta.com/blog/meta-llama-3/)           | 45.9    |
| Gemma 7B         | [Link](https://ai.meta.com/blog/meta-llama-3/)           | 44.9    |
| Mistral 7B       | [Link](https://ai.meta.com/blog/meta-llama-3/)           | 44      |

## AGIEval-zh few-shot

| Model            | Source                                                   | Average |
|------------------|----------------------------------------------------------|---------|
| GPT-4o           | [Link](https://github.com/ruixiangcui/AGIEval)           | 71.9    |
| GPT-3.5-Turbo    | [Link](https://github.com/ruixiangcui/AGIEval)           | 49.5    |

## AGIEval-all few-shot

| Model            | Source                                                   | Average |
|------------------|----------------------------------------------------------|---------|
| GPT-4o           | [Link](https://github.com/ruixiangcui/AGIEval)           | 69.0    |
| GPT-3.5-Turbo    | [Link](https://github.com/ruixiangcui/AGIEval)           | 47.2    |

## AGIEval-en zero-shot

| Model            | Source                                                   | Average |
|------------------|----------------------------------------------------------|---------|
| GPT-4o           | [Link](https://github.com/ruixiangcui/AGIEval)           | 65.2    |
| GPT-3.5-Turbo    | [Link](https://github.com/ruixiangcui/AGIEval)           | 54.1    |

## AGIEval-zh zero-shot

| Model            | Source                                                   | Average |
|------------------|----------------------------------------------------------|---------|
| GPT-4o           | [Link](https://github.com/ruixiangcui/AGIEval)           | 63.3    |
| GPT-3.5-Turbo    | [Link](https://github.com/ruixiangcui/AGIEval)           | 45.0    |


## AGIEval-all zero-shot
(Asterisk sign indicates results reported for AGIEval v1.0.)

| Model            | Source                                                   | Average |
|------------------|----------------------------------------------------------|---------|
| GPT-4o           | [Link](https://github.com/ruixiangcui/AGIEval)           | 62.3    |
| InternLM2-20B*   | [Link](https://arxiv.org/pdf/2403.17297)                 | 53.0    |
| Qwen-14B*        | [Link](https://arxiv.org/pdf/2403.17297)                 | 52.0    |
| Phi-3-medium 14b*| [Link](https://arxiv.org/pdf/2404.14219)                 | 50.2    |
| InternLM2-Chat-7B-SFT*| [Link](https://arxiv.org/pdf/2403.17297)            | 49.0    |
| GPT-3.5-Turbo    | [Link](https://github.com/ruixiangcui/AGIEval)           | 46.0    |
| Qwen-7B*         | [Link](https://arxiv.org/pdf/2403.17297)                 | 45.6    |
| Mixtral 8x7b*    | [Link](https://arxiv.org/pdf/2404.14219)                 | 45.2    |
| Phi-3-small 7b*  | [Link](https://arxiv.org/pdf/2404.14219)                 | 45.1    |
| Gemma 7b*        | [Link](https://arxiv.org/pdf/2404.14219)                 | 42.1    |
| Llama-3-In*      | [Link](https://arxiv.org/pdf/2404.14219)                 | 42.0    |
| Phi-3-mini 3.8b* | [Link](https://arxiv.org/pdf/2404.14219)                 | 37.5    |
| Mistral 7b*      | [Link](https://arxiv.org/pdf/2404.14219)                 | 35.1    |
| Phi-2 2.7b*      | [Link](https://arxiv.org/pdf/2404.14219)                 | 29.8    |

# Citation
If you use AGIEval benchmark or the code in your research, please cite our paper:
```
@misc{zhong2023agieval,
      title={AGIEval: A Human-Centric Benchmark for Evaluating Foundation Models}, 
      author={Wanjun Zhong and Ruixiang Cui and Yiduo Guo and Yaobo Liang and Shuai Lu and Yanlin Wang and Amin Saied and Weizhu Chen and Nan Duan},
      year={2023},
      eprint={2304.06364},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

# Contributing
This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

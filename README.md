# Papers in the CVPR 2023 Diffusion Model Tutorial

This repository contains a list of papers to include in the CVPR 2023 tutorial ["Denoising Diffusion Models:
A Generative Learning Big Bang"](https://cvpr2023-tutorial-diffusion-models.github.io/), by Jiaming Song, Chenlin Meng, and Arash Vahdat. 

As the number of papers are growing quite rapidly, it is impossible to list or even carefully read every paper in this field. 
Therefore, we take an "RLHF" approach to our tutorial and welcome any community feedback, to ensure we don't miss interesting / important works by accident (could be yours, could be others').

## Disclaimers

1. The goal of the tutorial is to provide a **high-level introduction** to researchers not familiar with diffusion models, or wish to be more familiar with its more recent developments related to CVPR. 
2. The field is growing at a near-exponential rate[^1]. Therefore, we have to consider **a curated list of selected papers**. We do not aim to make another paper tracker on diffusion models[^2].
3. Even in the curated list, your paper might not get highlighted (i.e., taking at least 3 mins in the tutorial) in the 3-hour talk.
4. Given the time constraint (1 hour x 3 sections), we can only highlight no more than 20 papers in each hour of the tutorial.
5. **We will make the final decisions regarding which papers get highlighted**, and we try to lean on papers with novel yet highly practical ideas.
6. That being said, we will list all the papers contributed here in our slides, and strive to give a "shout out" to many of them (e.g., one or two sentences listing their connections to highlighted work), as long as they are related to the topics in the tutorial.
7. Although we use the term "paper", it does not have to be a paper at all. The community has lots of amazing ideas that are not always presnted as a paper, and these are worth highlighting as well (an example is negative prompting). 
8. The deadline for contributions is **June 9th**, around ten days before the actual tutorial. 

[^1]: The awesome diffusion models repo (https://github.com/heejkoo/Awesome-Diffusion-Models) already lists more than 1300 papers on the topic, and that are even not all of them! 
[^2]: Several trackers are here: https://github.com/heejkoo/Awesome-Diffusion-Models (about 1300 papers as of writing), https://vsehwag.github.io/blog/2023/2/all_papers_on_diffusion.html (about 500 papers), https://scorebasedgenerativemodeling.github.io/ (about 800 papers).

## Contributions

We welcome all types of contributions, mostly in the form of papers under certain topics relevant to CVPR. For now, these include:

- **Fundamentals [Arash]**: these include methods that can be applied to general domains, such as training, sampling, guidance. 
- **Applications on natural iamges [Chenlin]**: these include applications that stem from natural images but can also be applied to other domains, such as architecture, editing, personalization, fine-tuning, "low-level" vision.
- **Applications on other domains [Jiaming]**: these include applications from other domains, such as video, 3d, motion, large content generation, inverse problems for medical domains, etc.

### New topics
If you think a paper does not fall into any of the topics that we listed, please raise an issue.

### New papers
If you want to contribute new "papers", please create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

Generally, we recommend adding papers in "Awesome Diffusion Models" format. If you are the author and you have some slides for the work, you can create a link to the slides as well. 

### Questions or suggestions

Please create an issue or send an email to jiaming [dot] tsong [at] "Google's personal email service in the US" [dot] com.

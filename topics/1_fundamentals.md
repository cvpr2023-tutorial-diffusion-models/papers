# Fundamentals of Diffusion Models

## Training

**Denoising Diffusion Probabilistic Models** \
*Jonathan Ho, Ajay Jain, Pieter Abbeel* \
NeurIPS 2020. [[Paper](https://arxiv.org/abs/2006.11239)] [[Github](https://github.com/hojonathanho/diffusion)] [[Github2](https://github.com/pesser/pytorch_diffusion)] \
19 Jun 2020 

**Score-Based Generative Modeling through Stochastic Differential Equations** \
*Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, Ben Poole* \
ICLR 2021 (Oral). [[Paper](https://arxiv.org/abs/2011.13456)] [[Github](https://github.com/yang-song/score_sde)] \
26 Nov 2020 

**Variational Diffusion Models** \
*Diederik P. Kingma<sup>1</sup>, Tim Salimans<sup>1</sup>, Ben Poole, Jonathan Ho* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2107.00630)] [[Github](https://github.com/google-research/vdm)] \
1 Jul 2021 

**Elucidating the Design Space of Diffusion-Based Generative Models** \
*Tero Karras, Miika Aittala, Timo Aila, Samuli Laine* \
NeurIPS 2022. [[Paper](https://arxiv.org/abs/2206.00364)] \
1 Jun 2022


## Fast sampling without additional training

**Denoising Diffusion Implicit Models**  \
*Jiaming Song, Chenlin Meng, Stefano Ermon* \
ICLR 2021. [[Paper](https://arxiv.org/abs/2010.02502)] [[Github](https://github.com/ermongroup/ddim)] \
6 Oct 2020

**Gotta Go Fast When Generating Data with Score-Based Models** \
Alexia Jolicoeur-Martineau, Ke Li, Rémi Piché-Taillefer, Tal Kachman, Ioannis Mitliagkas* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2105.14080)] [[Github](https://github.com/AlexiaJM/score_sde_fast_sampling)] \
28 May 2021

**Pseudo Numerical Methods for Diffusion Models on Manifolds** \
*Luping Liu, Yi Ren, Zhijie Lin, Zhou Zhao* \
ICLR 2022. [[Paper](https://arxiv.org/abs/2202.09778)] [[Github](https://github.com/luping-liu/PNDM)] \
20 Feb 2022

**DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Model Sampling in Around 10 Steps** \
*Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongxuan Li, Jun Zhu* \
NeurrIPS 2022. [[Paper](https://arxiv.org/abs/2206.00927)] [[Github](https://github.com/LuChengTHU/dpm-solver)] \
2 Jun 2022

**DPM-Solver++: Fast Solver for Guided Sampling of Diffusion Probabilistic Models** \
*Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongxuan Li, Jun Zhu* \
NeurIPS 2022 (Oral). [[Paper](https://arxiv.org/abs/2211.01095)] [[Github](https://github.com/LuChengTHU/dpm-solver)] \
2 Nov 2022

**Fast Sampling of Diffusion Models with Exponential Integrator** \
*Qinsheng Zhang, Yongxin Chen* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2204.13902)] \
29 Apr 2022

**gDDIM: Generalized denoising diffusion implicit models** \
*Qinsheng Zhang, Molei Tao, Yongxin Chen* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2206.05564)] [[Github](https://github.com/qsh-zh/gDDIM)] \
11 Jun 2022

**UniPC: A Unified Predictor-Corrector Framework for Fast Sampling of Diffusion Models** \
*Wenliang Zhao, Lujia Bai, Yongming Rao, Jie Zhou, Jiwen Lu* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2302.04867)] [[Project](https://unipc.ivg-research.xyz)] [[Github](https://github.com/wl-zhao/UniPC)] \
9 Feb 2023




## Fast sampling with additional training

**Tackling the Generative Learning Trilemma with Denoising Diffusion GANs** \
*Zhisheng Xiao, Karsten Kreis, Arash Vahdat* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2112.07804)] [[Project](https://nvlabs.github.io/denoising-diffusion-gan)] \
15 Dec 2021

**Progressive Distillation for Fast Sampling of Diffusion Models** \
*Tim Salimans, Jonathan Ho* \
ICLR 2022. [[Paper](https://arxiv.org/abs/2202.00512)] \
1 Feb 2022

**On Distillation of Guided Diffusion Models** \
*Chenlin Meng, Ruiqi Gao, Diederik P. Kingma, Stefano Ermon, Jonathan Ho, Tim Salimans* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.03142)] \
6 Oct 2022

**GENIE: Higher-Order Denoising Diffusion Solvers** \
*Tim Dockhorn, Arash Vahdat, Karsten Kreis* \
NeurIPS 2022 (Oral). [[Paper](https://arxiv.org/abs/2210.05475)] [[Github](https://github.com/nv-tlabs/GENIE)] \
11 Oct 2022

**Learning Fast Samplers for Diffusion Models by Differentiating Through Sample Quality** \ 
*Daniel Watson, William Chan, Jonathan Ho, Mohammad Norouzi* \
ICLR 2022. [[Paper](https://arxiv.org/abs/2202.05830)] \
11 Feb 2022

**Wavelet Diffusion Models Are Fast and Scalable Image Generators** \
*Hao Phung, Quan Dao, Anh Tran* \
CVPR 2023. [[Paper](https://arxiv.org/abs/2211.16152)] [[Github](https://github.com/VinAIResearch/WaveDiff.git)] \
29 Nov 2022

## Conditional Generation and Guidance

**Diffusion Models Beat GANs on Image Synthesis** \
*Prafulla Dhariwal<sup>1</sup>, Alex Nichol<sup>1</sup>* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2105.05233)] [[Github](https://github.com/openai/guided-diffusion)] \
11 May 2021 

**Classifier-Free Diffusion Guidance** \
*Jonathan Ho, Tim Salimans* \
NeurIPS Workshop 2021. [[Paper](https://arxiv.org/abs/2207.12598)] \
28 Sep 2021

**Negative Prompt** \
*Automatic1111* \
[[Report](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Negative-prompt)]

**Improving Sample Quality of Diffusion Models Using Self-Attention Guidance** \
*Susung Hong, Gyuseong Lee, Wooseok Jang, Seungryong Kim* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2210.00939)] [[Github](https://github.com/KU-CVLAB/Self-Attention-Guidance/)] \
3 Oct 2022 

## Diffusion Models on Low-dimensional Spaces

**Image Super-Resolution via Iterative Refinement** \
*Chitwan Saharia, Jonathan Ho, William Chan, Tim Salimans, David J. Fleet, Mohammad Norouzi* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2104.07636)] [[Project](https://iterative-refinement.github.io/)] [[Github](https://github.com/Janspiry/Image-Super-Resolution-via-Iterative-Refinement)] \
15 Apr 2021 

**Cascaded Diffusion Models for High Fidelity Image Generation** \
*Jonathan Ho<sup>1</sup>, Chitwan Saharia<sup>1</sup>, William Chan, David J. Fleet, Mohammad Norouzi, Tim Salimans* \
JMLR 2021. [[Paper](https://arxiv.org/abs/2106.15282)] [[Project](https://cascaded-diffusion.github.io/)] \
30 May 2021 

**D2C: Diffusion-Denoising Models for Few-shot Conditional Generation** \
*Abhishek Sinha<sup>1</sup>, Jiaming Song<sup>1</sup>, Chenlin Meng, Stefano Ermon* \
NeurIPS 2021. [[Paper](https://arxiv.org/abs/2106.06819)] [[Project](https://d2c-model.github.io/)] [[Github](https://github.com/d2c-model/d2c-model.github.io)] \
12 Jun 2021

**Score-based Generative Modeling in Latent Space** \
*Arash Vahdat<sup>1</sup>, Karsten Kreis<sup>1</sup>, Jan Kautz* \
arXiv 2021. [[Paper](https://arxiv.org/abs/2106.05931)] \
10 Jun 2021

**High-Resolution Image Synthesis with Latent Diffusion Models** \
*Robin Rombach<sup>1</sup>, Andreas Blattmann<sup>1</sup>, Dominik Lorenz, Patrick Esser, Björn Ommer* \
CVPR 2022. [[Paper](https://arxiv.org/abs/2112.10752)] [[Github](https://github.com/CompVis/latent-diffusion)] \
20 Dec 2021

**Score-Guided Intermediate Layer Optimization: Fast Langevin Mixing for Inverse Problems** \
*Giannis Daras<sup>1</sup>, Yuval Dagan<sup>1</sup>, Alexandros G. Dimakis, Constantinos Daskalakis* \
ICML 2022. [[Paper](https://arxiv.org/abs/2206.09104)] [[Github](https://github.com/giannisdaras/sgilo)] \
22 Jun 2022


## Generalized Diffusion Models

**Cold Diffusion: Inverting Arbitrary Image Transforms Without Noise** \
*Arpit Bansal, Eitan Borgnia, Hong-Min Chu, Jie S. Li, Hamid Kazemi, Furong Huang, Micah Goldblum, Jonas Geiping, Tom Goldstein* \
arXiv 2022. [[Paper](https://arxiv.org/abs/2208.09392)] [[Github](https://github.com/arpitbansal297/Cold-Diffusion-Models)] \
19 Aug 2022

**Soft Diffusion: Score Matching for General Corruptions** \
*Giannis Daras, Mauricio Delbracio, Hossein Talebi, Alexandros G. Dimakis, Peyman Milanfar* \
TMLR 2023. [[Paper](https://openreview.net/forum?id=W98rebBxlQ)] \
12 Sep 2022

**Inversion by Direct Iteration: An Alternative to Denoising Diffusion for Image Restoration** \
*Mauricio Delbracio, Peyman Milanfar* \
arXiv 2023. [[Paper](https://arxiv.org/abs/2303.11435)] \
20 March 2023



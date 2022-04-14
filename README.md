# YouTube-Commenter
To be able to use the project one should obtain authorization credentials following the steps described at: https://developers.google.com/youtube/registering_an_application


* The main purpose of this project is to automate the process of writting comments under YouTube videos.
* The project's comment generation is enabled with the help of GPT2-a transformers model.
* To post comments we use YouTube Data Api.
* We also provide some additional features via our "YoutubeApi" class to enable video related and channel related metadata   retreval such as num of viewrs, most popular videos of the channel etc.

Limitations: 
The main limitation of the project is in the text generation section. Specifically, GPT-2 is pretrained on a very large corpus of English data (40 GB) in a self-supervised fashion. However, we think that the data is not well suitable for our purposes since comments in YouTube tend to be short texts with the usage of slang words (sometimes) & overall are more informal than the text upon which the GPT-2 was trained.
Hence, a further work can be to acquire some comments dataset from YouTube and train GPT-2 or any other desired model on it to get (presumably) better results at YouTube comment generation.
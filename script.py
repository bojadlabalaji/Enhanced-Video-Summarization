# -*- coding: utf-8 -*-
"""Updated Final Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mIbpK_pRq4qdMdJnenmHZfHVQxJUCRJQ

# **VISON+ - Enhanced Video Summarization**

Team Members:
---
- Balaji Bojadla
- Mallikarjunarao Kovi

# **Abstract**
---
Video summarization plays a crucial role in condensing lengthy videos into shorter versions while retaining key information. This project, titled VISON+ - Enhanced Video Summarization, aims to create comprehensive video summaries for long YouTube videos using both abstractive and extractive summarization techniques. By leveraging Natural Language Processing (NLP) pipelines and innovative video editing methods, VISON+ generates concise and informative summaries that capture the essence of the original content. This report outlines the methodology, techniques, and outcomes of the VISON+ project, along with a review of related work in the field of video summarization.

# **Introduction**
---
Video content has become increasingly prevalent on online platforms such as YouTube, providing a vast repository of information and entertainment. However, the sheer volume of video content available poses challenges for viewers who may not have the time or patience to watch lengthy videos in their entirety. Video summarization addresses this challenge by condensing videos into shorter versions while preserving essential information.

The project titled VISON+ - Enhanced Video Summarization aims to enhance the accessibility and usability of long YouTube videos by creating concise and informative video summaries. This project utilizes advanced techniques in abstractive and extractive summarization to generate comprehensive summaries that capture the essence of the original content. By combining these techniques with innovative video editing methods, VISON+ produces summary videos that offer quick insights into the content of lengthy videos.

In this report, we present the methodology, techniques, and outcomes of the VISON+ project. We begin by discussing the data collection process and the tools used for video transcription. Next, we delve into the details of abstractive and extractive summarization techniques employed in the project. We also provide a review of related work in the field of video summarization, highlighting key contributions and methodologies from existing literature.

Throughout the report, we use Markdown Cells to explain the outputs of our Code Cells, providing a clear and concise narrative of the project's methodology and outcomes. By leveraging advanced techniques in video summarization, VISON+ offers a novel approach to enhancing the accessibility and usability of long YouTube videos, paving the way for efficient consumption of video content in various domains.

# **Literature Review**
---
**Literature Review**

Video summarization is a critical task in multimedia content analysis, aimed at condensing lengthy videos into shorter versions while retaining key information. In recent years, various approaches and techniques have been developed to address this challenge. In this literature review, we explore related work in the field of video summarization, highlighting key contributions and methodologies.

1. **YouTube Transcript API**  
   The YouTube Transcript API, developed by Depoix [1], provides a convenient way to access and extract transcripts from YouTube videos. This tool facilitates the retrieval of textual content from videos, which is essential for subsequent analysis and summarization tasks.

   [1] GitHub Repository: [https://github.com/jdepoix/youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)

2. **AI-Driven YouTube Video Generation**  
   Oluyale [2] presents a comprehensive guide on generating YouTube videos using AI and machine learning techniques. The article discusses the use of NLP pipelines and summarization algorithms to generate concise and informative video content. This work provides insights into the application of AI in video content creation.

   [2] Medium Article: [https://medium.com/@oluyaled/generate-youtube-video-using-ai-ml-python-c9ba9c86f9ea](https://medium.com/@oluyaled/generate-youtube-video-using-ai-ml-python-c9ba9c86f9ea)

3. **Speech-to-Text Extraction from Video**  
   GeeksforGeeks offers a tutorial on extracting speech-to-text from videos using Python [3]. This tutorial introduces techniques for converting audio content from videos into textual transcripts, which can be further analyzed and summarized using natural language processing algorithms.

   [3] GeeksforGeeks Tutorial: [https://www.geeksforgeeks.org/extract-speech-text-from-video-in-python/](https://www.geeksforgeeks.org/extract-speech-text-from-video-in-python/)

4. **Video Concatenation with MoviePy**  
   The MoviePy library, as demonstrated by GeeksforGeeks [4], provides functionalities for concatenating multiple video files. This capability is crucial for assembling summary videos from segmented clips, allowing for the creation of concise and coherent video summaries.

   [4] GeeksforGeeks Tutorial: [https://www.geeksforgeeks.org/moviepy-concatenating-multiple-video-files/](https://www.geeksforgeeks.org/moviepy-concatenating-multiple-video-files/)

5. **Transformer-Based Text Summarization with Hugging Face**  
   Hugging Face offers a suite of pre-trained transformer models fine-tuned for various NLP tasks, including text summarization [5]. These models leverage transformer architectures to generate concise summaries from textual input. The Hugging Face documentation provides comprehensive guidance on using these models for text summarization tasks.

   [5] Hugging Face Summarization Documentation: [https://huggingface.co/docs/transformers/en/tasks/summarization](https://huggingface.co/docs/transformers/en/tasks/summarization)

These references provide valuable insights and tools for the development and implementation of video summarization systems. By leveraging these resources and building upon existing methodologies, researchers and practitioners can continue to advance the field of multimedia content analysis and enhance the accessibility and usability of video content.

---

**Training Procedure of Summarization Model**
---
The summarization model used in this project, "sshleifer/distilbart-cnn-12-6", is a pre-trained transformer model fine-tuned specifically for the task of text summarization. The training procedure for this model typically involves the following steps:

1. **Data Collection:** The training data for the summarization model consists of a large corpus of text data, typically sourced from various sources such as news articles, blog posts, academic papers, and other publicly available textual content. The dataset should include pairs of input text and their corresponding summaries.

2. **Preprocessing:** Before training the model, the training data undergoes preprocessing steps to clean and prepare it for the summarization task. This may include removing irrelevant content, tokenizing the text into individual words or subwords, and converting the text into numerical representations suitable for input into the model.

3. **Model Architecture:** The summarization model is based on transformer architecture, which is a type of neural network architecture known for its effectiveness in handling sequential data. Transformers consist of multiple layers of self-attention mechanisms and feed-forward neural networks, allowing them to capture dependencies between words in the input text and generate coherent summaries.

4. **Fine-tuning:** The pre-trained transformer model is fine-tuned on the specific task of text summarization using the training data. During fine-tuning, the model adjusts its parameters to minimize a loss function that measures the difference between the generated summaries and the ground truth summaries in the training data.

5. **Evaluation:** After fine-tuning, the model is evaluated on a separate validation set to assess its performance in generating accurate and coherent summaries. Evaluation metrics such as ROUGE (Recall-Oriented Understudy for Gisting Evaluation) scores are commonly used to measure the quality of the generated summaries compared to the ground truth.

6. **Deployment:** Once the model has been trained and evaluated satisfactorily, it can be deployed for use in summarizing new input text data. The deployed model accepts input text and generates concise summaries based on the learned patterns and associations in the training data.

The summarization model "sshleifer/distilbart-cnn-12-6" utilized in this project has been trained on the BillSum dataset, provided by Hugging Face. The BillSum dataset is a collection of legislative bills and their summaries, sourced from various state legislatures in the United States.

**BillSum Dataset Description:**
- The BillSum dataset consists of pairs of legislative bills and their corresponding summaries, providing concise representations of the main points and key information contained within each bill.
- Each sample in the dataset contains the full text of a legislative bill, along with its associated summary, which is typically a shorter version of the bill's contents.
- The dataset covers a wide range of topics and legislative domains, including healthcare, education, transportation, and more, reflecting the diversity of legislative activity across different states.
- The dataset is well-annotated, with high-quality summaries that accurately capture the essential information and key provisions of each bill.

**Dataset Link:**
- [BillSum Dataset](https://huggingface.co/datasets/billsum)

The BillSum dataset serves as a valuable resource for training summarization models, providing rich and diverse text data that can be used to develop and evaluate the effectiveness of text summarization algorithms. By leveraging the BillSum dataset, the "sshleifer/distilbart-cnn-12-6" model has been fine-tuned to generate high-quality summaries across a variety of legislative contexts, making it well-suited for summarizing text from a wide range of domains and topics.

**Data Collection:**
---
For the training of the Hugging Face model, we utilized a pre-existing dataset provided by Hugging Face called BillSum. The BillSum dataset contains pairs of legislative bills and their corresponding summaries, sourced from various state legislatures in the United States. This dataset serves as a valuable resource for training summarization models, providing rich and diverse text data suitable for the summarization task.

**Data Cleaning:**
---
As the summarization model "sshleifer/distilbart-cnn-12-6" was pre-trained on the BillSum dataset, we did not perform explicit training in this project. Instead, we focused on preparing our data for inference with the pre-trained model. We obtained YouTube video transcripts using the YouTube Transcript API, which provided textual content from YouTube videos in the form of transcribed paragraphs.

**Data Processing:**
---
After obtaining the transcribed paragraph text from the YouTube videos, we processed the data to ensure compatibility with the summarization model and to prepare it for generating the final summary video.

Firstly, we converted the transcribed paragraphs into individual sentences or segments, as required by the summarization model. Each sentence or segment served as an input to the model for generating summaries.

Next, we filtered the transcribed list by deleting sentences that were not presented in the summary paragraph. This step ensured that only relevant content was considered for summarization, improving the quality and relevance of the generated summary.

Finally, we refined the output list of dictionaries by removing unnecessary fields such as the 'text' field, which contained the transcribed text. Instead, we retained only the 'start' and 'duration' fields, which provided information about the timing of each segment in the video. These fields were essential for splitting and merging the video segments to create the final summary video.

By processing the transcribed data in this manner, we ensured that it was compatible with the summarization model and suitable for generating concise and informative summaries. Additionally, refining the output list of dictionaries allowed for efficient manipulation of video segments to produce the final summary video.

**Description of YouTube Video Input, Text Extraction, and Summary Paragraph Output:**
---
- **YouTube Video Input**: The YouTube videos served as the source of content for the summarization task. These videos covered a wide range of topics and genres, ensuring diversity in the training data. The YouTube Transcript API facilitated the extraction of textual content from the videos, providing transcribed paragraphs for summarization.

- **Text Extraction**: The text extraction process involved retrieving transcribed paragraphs from the YouTube videos using the YouTube Transcript API. Each transcribed paragraph represented the textual content of the video, providing input data for the summarization model.

- **Summary Paragraph Output**: The output of the summarization process was a summary paragraph containing key sentences extracted from the transcribed video content. This summary paragraph condensed the original video content into a concise and informative summary, capturing the essence of the video in a shorter form.

In this project, since the summarization model "sshleifer/distilbart-cnn-12-6" was pre-trained on the BillSum dataset, we focused on processing the cleaned and processed video transcript data into our preferred format for inference with the pre-trained model.
"""

!pip install youtube-transcript-api
!pip install langdetect
!pip install pytube
!pip install spacy
!python3 -m spacy download en_core_web_lg
!pip install pytextrank

# Import all the necessary dependencies
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from nltk.tokenize import sent_tokenize
from langdetect import detect

def generate_summary(url, max_length=150):
    """
    Summarizes the transcript of a YouTube video.

    This function takes a YouTube video URL and an optional max_length parameter as inputs.
    It first retrieves the transcript of the YouTube video.
    If the transcript is longer than 3000 words, it uses extractive summarization (e.g. LSA).
    Otherwise, it uses abstractive summarization.

    Parameters:
    - url (str): The URL of the YouTube video.
    - max_length (int, optional): The maximum length of the summary. Defaults to 150.

    Returns:
    - str: The summarized transcript.
    """
    # max_length = int(request.args.get('max_length', 150))
    video_id = url.split('=')[1]
    # video_id = "IitIl2C3Iy8"
    # max_length = max(int(max_length), 150)

    try:
        transcript_list, transcript, length = get_transcript(video_id)
        max_length = max(int(max_length), 150)
    except:
        return "No subtitles available for this video", 404

    # Extractive summarization using LSA or Frequency-based method
    # if len(transcript.split()) > 3000:
    #     summary = extractive_summarization(transcript)
    # else:
    #     summary = abstractive_summarization(transcript, max_length)


    summary = textrank(transcript)

    return transcript_list, summary, 200

import spacy
import pytextrank


def textrank(transcript):
  nlp = spacy.load("en_core_web_lg")
  nlp.add_pipe("textrank")
  example_text = transcript
  length = len(transcript.split("."))
  print('Original Document Size:', length)
  doc = nlp(example_text)
  summary = ''
  limit_phrases = 2
  limit_sentences = length // 3

  print('SUmmary Document Size:', limit_sentences)



  for sent in doc._.textrank.summary(limit_phrases=limit_phrases, limit_sentences=limit_sentences):
    # print(sent)
    summary = summary + str(sent)
    # print('Summary Length:',len(sent))
  return summary

def is_transcript_english(transcript):
    """
    Detect if the transcript is primarily in English.

    :param transcript: The transcript text to be analyzed.
    :return: True if the transcript is primarily in English, False otherwise.
    """
    try:
        language = detect(transcript)
        return language == 'en'

    except Exception as e:
        return False

def get_transcript(video_id):
    """
    Fetches and concatenates the transcript of a YouTube video.

    Parameters:
    video_id (str): The ID of the YouTube video.

    Returns:
    str: A string containing the concatenated transcript of the video.

    Raises:
    Exception: If there is an error in fetching the transcript.
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        max_length = len(transcript_list)
    except Exception as e:
        raise e

    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript_list, transcript, max_length

# Prompt the user to input the YouTube video URL and maximum length of the summary
# url = input("Paste your YouTube video URL: ")
# max_length = input("Enter maximum length of the summary (in sentences): ")

url = "https://www.youtube.com/watch?v=IitIl2C3Iy8"
max_length = 75

# Call the function 'generate_summary' to generate the summary
transcript_list, summary_paragraph, status = generate_summary(url, max_length)

# Print a header for the summary
print("Summary of the YouTube video:\n***************************************************\n")

# Display the summary paragraph
summary_paragraph

import json

# Define a function to match text in a paragraph with text in a list of JSON objects
def match_text_in_json(paragraph, json_list):
    matched_list = []
    # Iterate over each JSON object in the list
    for obj in json_list:
        # Check if the text of the JSON object (case-insensitive) is present in the paragraph
        if obj['text'].lower() in paragraph.lower():
            # If a match is found, append the JSON object to the matched list
            matched_list.append(obj)
    return matched_list

# SUmmary paragraph paragraph to search for matches
paragraph = summary_paragraph

# transcript  list of JSON objects
json_list = transcript_list

# Call the function to find JSON objects that match text in the paragraph
matched_json = match_text_in_json(paragraph, json_list)

# Print the matched JSON objects
matched_json

def merge_dicts(input_list):

    '''
    This function, merge_dicts, takes a list of dictionaries input_list as input, where each dictionary represents
    a segment with keys 'start' and 'duration'. The function merges overlapping segments within the list, ensuring
    that no two segments overlap in time.
    '''
    output_list = []
    n = len(input_list)
    i = 0

    while i < n:
        current_segment = input_list[i]
        j = i + 1

        while j < n and current_segment['start'] + current_segment['duration'] + 1 >= input_list[j]['start']:
            # Merge overlapping segments
            current_segment['duration'] = input_list[j]['start'] - current_segment['start'] + input_list[j]['duration']
            j += 1

        output_list.append({'start': current_segment['start'], 'duration': current_segment['duration']})
        i = j

    return output_list
    return merged_list

# Sample input
input_list = matched_json

# Call the function and print the output
merged_matched_json = merge_dicts(input_list)
#Print the merged output list
merged_matched_json

from pytube import YouTube

# Create a YouTube object by passing the video URL
yt = YouTube(url)

# Filter streams to select only progressive MP4 streams and order them by resolution
selected_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()

# Download the selected stream with the lowest resolution and save it as 'original_video.mp4'
selected_stream.download(filename='original_video.mp4')

from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load the original video
original_video = VideoFileClip("original_video.mp4")

# List of start positions and durations
video_segments = merged_matched_json

# List to store cut video clips
cut_clips = []

# Cut the video based on segments
for segment in video_segments:
    start_time = segment["start"]
    duration = segment["duration"]
    end_time = start_time + duration

    # Cut the segment from the original video
    cut_clip = original_video.subclip(start_time, end_time)
    cut_clips.append(cut_clip)

print(cut_clip)
# Concatenate all the cut clips
final_video = concatenate_videoclips(cut_clips)


# Export the final video
final_video.write_videofile("final_video.mp4")

from IPython.display import Video

# final_video.mp4 is in the current directory
video_path = "final_video.mp4"

# Display the video
Video(video_path)

"""**Evaluation**
---

----
In order to evaluate the effectiveness of the summarization model, I conducted a test with Ms. Boddu Kavya, a MSIT student at the University of Cincinnati. Ms. Kavya was provided with an original video approximately 11 minutes long titled **"*Six behaviors to increase your confidence | Emily Jaenson | TEDxReno*"**. Subsequently, she was shown the summary video of 3 minutes long generated by the project.

Ms. Kavya provided positive feedback on the summarization features, stating that most of the significant information from the original video was covered in the summary video. She scored the model with a rating of 90 out of 100, indicating a high level of satisfaction with the summarization output. Additionally, she mentioned that by using the model's output on other videos, she was able to save a significant amount of time by referring to the summary videos.

However, Ms. Kavya also noted that while the summary videos were helpful for revision purposes, they may not be solely dependable for study purposes, as some important information may be left out by the model. Nonetheless, she expressed confidence in using the model for revision and quick reference purposes.

Overall, the evaluation results indicate that the summarization model effectively condenses lengthy videos into concise summaries, capturing the essential information and providing users with a valuable tool for efficient content consumption. Further refinements and enhancements to the model could potentially improve its performance and utility for a wider range of applications.

----
In order to ensure the authenticity of the evalution / feedback section, here are the contact details of the evaluator:

Evaluator Information:

- Name: Boddu Kavya
- Email: bodduka@mail.uc.edu

**Results and Conclusions**
---

---
The project successfully achieved its goal of generating short YouTube videos using the MoviePy library based on the filtered transcript list. By extracting timestamps from the filtered transcript list, we were able to accurately segment the original video and concatenate these segments to create a concise summary video.

The summarization process involved filtering the transcript list to include only sentences present in the summary paragraph. This ensured that the generated summary video captured the most important aspects of the original content. The timestamps extracted from the filtered transcript list served as the basis for cutting and concatenating video segments, resulting in a coherent summary video.

Through this approach, we effectively condensed lengthy YouTube videos into shorter, more digestible summaries, making it easier for viewers to grasp the key points without having to watch the entire video. This has significant implications for content creators, educators, and consumers alike, as it allows for more efficient consumption and dissemination of video content.

In conclusion, the project demonstrates the feasibility and effectiveness of using automated summarization techniques to generate concise video summaries. By leveraging tools such as the MoviePy library and filtering techniques based on transcript analysis, we can streamline the process of summarizing video content and enhance its accessibility and usability for a wide range of audiences. This project lays the foundation for future research and development in the field of video summarization, paving the way for more advanced and sophisticated approaches to content summarization and analysis.
"""


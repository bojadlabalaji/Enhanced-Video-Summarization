# Efficient Generation of Summary Videos from Long-form Content
By utilizing advanced Natural Language Processing (NLP) pipelines and state-of-the-art video editing techniques, this project produces concise and informative summaries that effectively capture the essence of the original content through extractive summarization.


## Introduction

This project aims to generate summary videos from long YouTube videos by following these steps:
1. Downloading a long YouTube video.
2. Transcribing the video into text (English only).
3. Summarizing the transcribed text using extractive summarization.
4. Extracting timestamps of each sentence in the summary paragraph.
   1. Merging adjacent timestamps to reduce the number of video segments.
5. Segmenting the video using the extracted timestamps.
6. Merging all the extracted video segments to create the final summary video.

## Installation

To set up the environment for this project, follow these steps:

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Download the SpaCy model:

    ```bash
    python -m spacy download en_core_web_lg
    ```

## Usage

To run the project, follow these steps:

1. Import the necessary libraries and install additional packages if required:

    ```python
    !pip install youtube-transcript-api langdetect pytube spacy pytextrank
    !python3 -m spacy download en_core_web_lg
    ```

2. Download the YouTube video:

    ```python
    from pytube import YouTube

    yt = YouTube(url)
    selected_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()
    selected_stream.download(filename='original_video.mp4')
    ```

3. Transcribe the video to text using `youtube-transcript-api` and perform extractive summarization (specific implementation details should be in your script).

4. Match the summary paragraph in the transcribed JSON list:

    ```python
    matched_json = match_text_in_json(paragraph, json_list)
    ```

5. Merge overlapping segments:

    ```python
    def merge_dicts(input_list):
        output_list = []
        n = len(input_list)
        i = 0

        while i < n:
            current_segment = input_list[i]
            j = i + 1

            while j < n and current_segment['start'] + current_segment['duration'] + 1 >= input_list[j]['start']:
                current_segment['duration'] = input_list[j]['start'] - current_segment['start'] + input_list[j]['duration']
                j += 1

            output_list.append({'start': current_segment['start'], 'duration': current_segment['duration']})
            i = j

        return output_list

    merged_matched_json = merge_dicts(matched_json)
    ```

6. Segment and merge the video:

    ```python
    from moviepy.editor import VideoFileClip, concatenate_videoclips

    original_video = VideoFileClip("original_video.mp4")
    video_segments = merged_matched_json

    clips = []
    for segment in video_segments:
        start = segment['start']
        duration = segment['duration']
        clip = original_video.subclip(start, start + duration)
        clips.append(clip)

    summary_video = concatenate_videoclips(clips)
    summary_video.write_videofile("summary_video.mp4", codec="libx264")
    ```

## Results and Conclusions

The project successfully generates concise summary videos by filtering transcripts and extracting relevant segments. This approach significantly reduces the time required to understand the main points of long videos, enhancing accessibility and usability for a wide range of audiences.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Original File

For detailed project information, refer to the original file located [here](https://colab.research.google.com/drive/1mIbpK_pRq4qdMdJnenmHZfHVQxJUCRJQ).

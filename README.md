# youtube-data-analysis
Data analysis of statistics from Top YouTube creators using Python and Youtube Data API v3

## Data

### Channels

The video data pulled from YouTube comes from ten of the top YouTube creators.
1. [PewDiePie](https://www.youtube.com/user/PewDiePie)
2. [MrBeast](https://www.youtube.com/user/MrBeast6000)
3. [DudePerfect](https://www.youtube.com/c/DudePerfect)
4. [Markiplier](https://www.youtube.com/c/markiplier)
5. [SSSniperWolf](https://www.youtube.com/c/SSSniperWolf)
6. [Dream](https://www.youtube.com/c/dream)
7. [jackscepticeye](https://www.youtube.com/c/jacksepticeye)
8. [VanossGaming](https://www.youtube.com/user/VanossGaming)
9. [Dobre Twins](https://www.youtube.com/c/LucasandMarcus)
10. [ZHC](https://www.youtube.com/c/ZHcomicart)

General channel data was pulled such as total views, likes, subscribers, etc.

### Videos

The program pulled the 200 most recent videos from each creator (or all videos if they had made less than 200 videos). This totals ~2000 videos worth of titles and statistics like likes, views, etc.

## Results

### Title WordClouds

Using the wordcloud python library, I generated wordclouds given all titles of the video data, and then one wordcloud for each channel.

![Overall WordCloud](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/wordclouds/overall.png?raw=true)

[Other WordClouds](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/wordclouds)

### Channel Comparison Results

Most Views by Channel

![Most Views](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_views_by_channel.png?raw=true)

Most Views in Set by Channel

![Most Views in Set](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_views_in_set.png?raw=true)

Most Views per Video by Channel

![Most Views per Video](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_views_per_vid.png?raw=true)

Most Views per Video in Set by Channel

![Most Views per Video in Set](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_views_per_vid_in_set.png?raw=true)

Most Likes per View by Channel

![Most Likes per View](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_likes_per_view.png?raw=true)

### Video Comparison Results

Most Viewed Videos

![Most Viewed Videos](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_viewed_videos.png?raw=true)

Most Liked Videos

![Most Liked Videos](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_liked_videos.png?raw=true)

### Title Analysis Results

Most Used Words in Titles

![Most Used Words](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_used_words.png?raw=true)

Most Viewed Words in Titles

![Most Viewed Words](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_viewed_words.png?raw=true)

Most Viewed Words per Videos Used in Titles

![Most Viewed Words per Videos](https://github.com/dfumo118/youtube-data-analysis/blob/main/img/graphs/most_viewed_words_per_vid.png?raw=true)

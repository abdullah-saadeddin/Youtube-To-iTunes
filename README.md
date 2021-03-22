# Youtube To iTunes

This python code download a video from <img width="15"  src="https://www.flaticon.com/svg/vstatic/svg/1384/1384060.svg?token=exp=1616389880~hmac=eda5618335e207f5fdfd92dd4cd5de15" alt="Youtube free icon" /> youtube as mp3 and add it to the <img width="15" src ="https://www.flaticon.com/svg/vstatic/svg/1384/1384061.svg?token=exp=1616390009~hmac=73b8207a5c51db1e1981bb5dbf468a8a" alt="iTunes"/>iTunes Library.

# Install && Run

```cmd
git clone https://github.com/abdullah-saadeddin/Youtube-To-iTunes.git
cd youtube-to-iTunes
pip install -r requirements.txt
python main.py
```

# How it works

I use the pytube Library to get the video from youtube using its URL, download the standard Quality of the video and get the thumbnail, the Library doesn't offer an mp3 file so I use the moviepy Library to convert the video to an mp3 file format after that, I downloaded the thumbnail using requests Library and finally add it to the mp3 file using eyed3 after all that the mp3 file moved to the iTunes Music Library folder which will sync it to iTunes.

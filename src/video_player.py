"""A video player class."""

from os import stat
from .video_library import VideoLibrary
from random import randint

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playing_video = None
        self._paused_video = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos.sort(key= lambda x: x.title)
        for i in videos:
            tags = " ".join(list(i.tags))
            print(f"\t {i.title} ({i.video_id}) [{tags}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        searched_item = self._video_library.get_video(video_id)

        #Check if the video exists
        if(searched_item is None):
            print("Cannot play video: Video does not exist")
        else:
            if self._playing_video is not None:
                self.stop_video()
            self._playing_video = searched_item
            self._paused_video = None
            print(f"Playing video: {self._playing_video.title}")


    def stop_video(self):
        """Stops the current video."""
        if self._playing_video is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self._playing_video.title}")
            self._playing_video = None
            self._paused_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()
        num_videos = len(videos)-1
        randomIndex = randint(0,num_videos)
        self.play_video(videos[randomIndex].video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self._playing_video is None:
            print("Cannot pause video: No video is currently playing")
        elif self._paused_video is not None:
            print(f"Video already paused: {self._paused_video.title}")
        else:
            self._paused_video = self._playing_video
            print(f"Pausing video: {self._paused_video.title}")


    def continue_video(self):
        """Resumes playing the current video."""

        if self._playing_video is None:
            print("Cannot continue video: No video is currently playing")
        elif self._paused_video is not None:
            print(f"Continuing video: {self._paused_video.title}")
            self._paused_video = None
        else:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""

        if self._playing_video is None:
            print("No video is currently playing")
        else:
            status = " - PAUSED" if self._paused_video is not None else ""
            video = self._video_library.get_video(self._playing_video.video_id)
            tags = " ".join(list(video.tags))
            print(f"Currently playing: {video.title} ({video.video_id}) [{tags}]{status}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

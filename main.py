import pytube
import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk


class App:

    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.title("YouTube Downloader")
        self.window_width = 500
        self.window_height = 400

        # Centering on screen
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Get center point
        center_x = int(self.screen_width/2 - self.window_width / 2)
        center_y = int(self.screen_height/2 - self.window_height / 2)
        self.root.geometry(
            f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        # First row for links
        self.url_label_frame = tk.LabelFrame(
            self.root, text="Enter url of video: ")
        self.url_label_frame.grid(
            row=0, column=0, columnspan=3, padx=3, pady=3)

        self.get_url = tk.Entry(self.url_label_frame,
                                width=79, selectborderwidth=10)
        self.get_url.grid(row=0, column=0, columnspan=3, pady=5, padx=5)

        self.get_url_button = tk.Button(
            self.url_label_frame, text="Check video", command=self.get_yt_object)
        self.get_url_button.grid(row=1, column=0, columnspan=3, pady=5, padx=5)

        # Second row for thumbnail
        self.video_info_holder = tk.LabelFrame(self.root, text="Video info ")
        self.video_info_holder.grid(row=1, column=0, padx=3, pady=3)

        self.show_title = tk.Label(self.video_info_holder, text="Author:")
        self.show_title.grid(row=0, column=0, pady=5, padx=5)

        self.show_title_value = tk.Label(self.video_info_holder)
        self.show_title_value.grid(row=0, column=1, pady=5, padx=5)

        self.show_age_restriction = tk.Label(
            self.video_info_holder, text="Age restriction:")
        self.show_age_restriction.grid(row=1, column=0, pady=5, padx=5)

        self.show_age_restriction_value = tk.Label(self.video_info_holder)
        self.show_age_restriction_value.grid(row=1, column=1, pady=5, padx=5)

        self.show_channel_url = tk.Label(
            self.video_info_holder, text="Channel URL:")
        self.show_channel_url.grid(row=2, column=0, pady=5, padx=5)

        self.show_channel_url_value = tk.Label(
            self.video_info_holder, text="Channel link", state="disabled")
        self.show_channel_url_value.grid(row=2, column=1, pady=5, padx=5)

        self.root.mainloop()

    def open_link(self, address):
        webbrowser.open_new(address)

    def set_info(self, author: str, age_restriction: bool, channel_url: str):
        # Setting author
        self.show_title_value.config(text=author)

        # Setting agee restriction
        self.show_age_restriction_value.config(text=age_restriction)

        # Setting channel url
        self.show_channel_url_value.config(state="active", cursor="hand2")
        self.show_channel_url_value.bind(
            "<Button-1>", lambda x:  self.open_link(channel_url))

    def get_yt_object(self):
        url_of_vid = self.get_url.get()
        try:
            pytube.YouTube(url=url_of_vid)

        except pytube.exceptions.RegexMatchError:
            messagebox.showerror("Error", "Invalid URL")

        else:
            yt_obj = pytube.YouTube(url=url_of_vid)
            # print(dir(yt_obj))
            self.set_info(yt_obj.author, yt_obj.age_restricted,
                          yt_obj.channel_url)
            print(yt_obj.description)
            print(yt_obj.length)
            print(yt_obj.publish_date)
            print(yt_obj.title)
            print(yt_obj.video_id)


if __name__ == "__main__":
    app = App()

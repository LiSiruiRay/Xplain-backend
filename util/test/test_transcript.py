# Author: ray
# Date: 9/16/23

import unittest

from util.transcript import get_transcript_detail, transcript_to_str, get_transcript_str, get_summarized_transcript, \
    binary_search_index


class MyTestCaseTranscript(unittest.TestCase):
    def test_transcript_getter(self):
        video_id = "78vN4sO7FVU"
        result = get_transcript_detail(video_id=video_id)
        print(f"type: {result}")

    def test_transcript_to_str(self):
        video_id = "78vN4sO7FVU"
        str_trans = get_transcript_str(video_id=video_id)
        print(str_trans)

    def test_get_summarized_transcript(self):
        video_id = "78vN4sO7FVU"
        summ = get_summarized_transcript(video_id=video_id)
        print(summ)

    def test_binary_search_index(self):
        video_id = "78vN4sO7FVU"
        result = get_transcript_detail(video_id=video_id)
        index = binary_search_index(460.52, result)
        correct = {'text': 'that if V is a\nBanach space, then', 'start': 460.52, 'duration': 2.85}
        print(result[index])

if __name__ == '__main__':
    unittest.main()

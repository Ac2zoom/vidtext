from rake_nltk import Rake
from google_images_download import google_images_download


def getImage(listData):
	r = Rake(min_length=1, max_length=10)
	li = listData
	r.extract_keywords_from_text(li)
	key_collection = r.get_ranked_phrases_with_scores()
	keyword = key_collection[0][1]
	response = google_images_download.googleimagesdownload()
	arguments = {
		"keywords": keyword,
		"suffix_keywords": "no watermark",
		"format": "jpg",
		"aspect_ratio": "wide",
		"usage_rights": "labeled-for-reuse-with-modifications",
		"limit": 1,
		"size": "large",
		"print_urls": True}
	response_paths = response.download(arguments)
	path = response_paths[0][keyword + " no watermark"][0]
	return path

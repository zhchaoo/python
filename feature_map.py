#!/usr/bin/python 
# coding: utf-8

import cookielib
import io
import json
import multiprocessing
import sys
import time
import urllib, urllib2

target_url = "http://100.84.43.126/fba/getFeatureJson.php"
max_feature_size = 50
feature_list = {}


# get feature info:
def get_feature_info_by_id(feature_id):
    data = {'feature': feature_id}
    f = urllib2.urlopen(
        url=target_url,
        data=urllib.urlencode(data)
    )
    html_text = f.read()
    start_index = html_text.find('[{"id":"')
    if start_index < 0:
        return -1
    end_index = html_text.find('}]', start_index)
    if end_index < 0:
        return -1
    return json.loads(html_text[start_index+1:end_index+1])


def main():
    for i in range(max_feature_size):
        feature = get_feature_info_by_id(i)
        if feature != -1:
            feature_list[feature['id']] = feature

    for feature in feature_list.values():
        print feature

    return 0;


# Main entry of the auto building tool
if __name__ == "__main__":
    sys.exit(main());

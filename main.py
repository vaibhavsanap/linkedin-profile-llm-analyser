# -*- coding: utf-8 -*-
import sys
import os
from scrapy.cmdline import execute


def gen_argv(s):
    sys.argv = s.split()


if __name__ == '__main__':

    user_id = input("Enter user linkedIn id: ")
    os.environ["USER_LINKEDIN_ID"] = user_id
    os.chdir("linkedin_scrapper")
    gen_argv('scrapy crawl linkedin_people_profile')
    execute()

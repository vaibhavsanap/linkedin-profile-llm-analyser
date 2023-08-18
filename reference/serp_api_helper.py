# # from serpapi import GoogleSearch
# #
# # params = {
# #   "engine": "linkedin",
# #   "first_name": "Jimmy",
# #   "last_name": "Neutron",
# #   "api_key": "fdc048b72d5beada104cc0f2b3b964dda5d4c9ada95894370f43e0bd27001a66"
# # }
# #
# # search = GoogleSearch(params)
# # results = search.get_dict()
# #
# # print(results)
#
#
# import os
#
# os.environ["GOOGLE_CSE_ID"] = "36a0b3ec13de4498a"
# os.environ["GOOGLE_API_KEY"] = "AIzaSyAdJUU5JHHC3uDMbawdbvt_CtyvEG-ttho"
#
#
# from langchain.tools import Tool
# from langchain.utilities import GoogleSearchAPIWrapper
#
# search = GoogleSearchAPIWrapper()
#
# tool = Tool(
#     name="Google Search",
#     description="Search Google for recent results.",
#     func=search.run,
# )
#
# tool.run("Obama's first name?")
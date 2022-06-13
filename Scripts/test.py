from Modules.read_TUV_resuls import TUV_results

params = {
    "path results": "../Results",
    "filename": "160106.txt",
    "hour initial": 6,
    "hour final": 20,
}

TUV = TUV_results()
TUV.read(params,
         params["filename"])

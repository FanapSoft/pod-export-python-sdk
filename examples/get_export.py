# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples import *
from pod_export import PodExport

try:
    pod_export = PodExport(api_token=API_TOKEN, server_type=SERVER_MODE)

    export_list = pod_export.get_export_list(serviceUrl="/nzh/biz/getInvoiceList/", sc_api_key=SC_API_KEY,
                                             sc_voucher_hash=SC_VOUCHER_HASH)
    print("Export List :\n", export_list)
    print("Total Export : ", pod_export.total_items())
    # OUTPUT
    # Export List :
    #  [
    #   {
    #       'id': 1510,
    #       'statusCode': 'EXPORT_SERVICE_STATUS_SUCCESSFUL',
    #       'creationDate': 1578382127057,
    #       'resultFile': {
    #           'id': 68083,
    #           'name': 'result-Tue Jan 07 07:29:00 UTC 2020.xlsx',
    #           'hashCode': '16f7e0000000000000004888519156',
    #           'size': 0
    #       },
    #       'service': '/nzh/biz/getInvoiceList/'
    #   },
    #   ...
    #   ]
    # Total Export :  21

    if len(export_list) > 0:
        export = export_list[0]

        request_info = pod_export.get_export(request_id=export["id"], sc_api_key=SC_API_KEY,
                                             sc_voucher_hash=SC_VOUCHER_HASH)
        print("Request Info :\n", request_info)
        # OUTPUT
        # Request Info :
        #   {
        #       'id': 1510,
        #       'statusCode': 'EXPORT_SERVICE_STATUS_SUCCESSFUL',
        #       'creationDate': 1578382127057,
        #       'resultFile': {
        #           'id': 68083,
        #           'name': 'result-Tue Jan 07 07:29:00 UTC 2020.xlsx',
        #           'hashCode': '16f7e0000000000000004888519156',
        #           'size': 0
        #       },
        #       'service': '/nzh/biz/getInvoiceList/'
        #   }

        download_link = pod_export.get_download_link(request_id=export["id"], sc_api_key=SC_API_KEY,
                                                     sc_voucher_hash=SC_VOUCHER_HASH)
        print("Download Link :", download_link)
        # OUTPUT
        # Download Link : http://sandbox.pod.ir:8080/nzh/file/?fileId=68083&hashCode=16f7e0000000000000004888519156

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

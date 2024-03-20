# coding: utf-8

"""
    API Reference

      # Introduction  Welcome to the REST API reference for the Zuora Billing, Payments, and Central Platform!  To learn about the common use cases of Zuora REST APIs, check out the [REST API Tutorials](https://developer.zuora.com/rest-api/api-guides/overview/).  In addition to Zuora API Reference, we also provide API references for other Zuora products:    * [Revenue API Reference](https://developer.zuora.com/api-references/revenue/overview/)   * [Collections API Reference](https://developer.zuora.com/api-references/collections/overview/)        The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Billing Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  Some of our older APIs are no longer recommended but still available, not affecting any existing integration. To find related API documentation, see [Older API Reference](https://developer.zuora.com/api-references/older-api/overview/).   ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Cloud 1 Production | https://rest.na.zuora.com  | |US Cloud 1 API Sandbox |  https://rest.sandbox.na.zuora.com | |US Cloud 2 Production | https://rest.zuora.com | |US Cloud 2 API Sandbox | https://rest.apisandbox.zuora.com| |US Central Sandbox | https://rest.test.zuora.com |   |US Performance Test | https://rest.pt1.zuora.com | |US Production Copy | Submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints. See [REST endpoint base URL of Production Copy (Service) Environment for existing and new customers](https://community.zuora.com/t5/API/REST-endpoint-base-URL-of-Production-Copy-Service-Environment/td-p/29611) for more information. | |EU Production | https://rest.eu.zuora.com | |EU API Sandbox | https://rest.sandbox.eu.zuora.com | |EU Central Sandbox | https://rest.test.eu.zuora.com |  The Production endpoint provides access to your live user data. Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision a Sandbox tenant for you, contact your Zuora representative for assistance.   If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.   # Error Handling  If a request to Zuora Billing REST API with an endpoint starting with `/v1` (except [Actions](https://developer.zuora.com/api-references/api/tag/Actions) and CRUD operations) fails, the response will contain an eight-digit error code with a corresponding error message to indicate the details of the error.  The following code snippet is a sample error response that contains an error code and message pair:  ```  {    \"success\": false,    \"processId\": \"CBCFED6580B4E076\",    \"reasons\":  [      {       \"code\": 53100320,       \"message\": \"'termType' value should be one of: TERMED, EVERGREEN\"      }     ]  } ``` The `success` field indicates whether the API request has succeeded. The `processId` field is a Zuora internal ID that you can provide to Zuora Global Support for troubleshooting purposes.  The `reasons` field contains the actual error code and message pair. The error code begins with `5` or `6` means that you encountered a certain issue that is specific to a REST API resource in Zuora Billing, Payments, and Central Platform. For example, `53100320` indicates that an invalid value is specified for the `termType` field of the `subscription` object.  The error code beginning with `9` usually indicates that an authentication-related issue occurred, and it can also indicate other unexpected errors depending on different cases. For example, `90000011` indicates that an invalid credential is provided in the request header.   When troubleshooting the error, you can divide the error code into two components: REST API resource code and error category code. See the following Zuora error code sample:  <a href=\"https://developer.zuora.com/images/ZuoraErrorCode.jpeg\" target=\"_blank\"><img src=\"https://developer.zuora.com/images/ZuoraErrorCode.jpeg\" alt=\"Zuora Error Code Sample\"></a>   **Note:** Zuora determines resource codes based on the request payload. Therefore, if GET and DELETE requests that do not contain payloads fail, you will get `500000` as the resource code, which indicates an unknown object and an unknown field.  The error category code of these requests is valid and follows the rules described in the [Error Category Codes](https://developer.zuora.com/api-references/api/overview/#section/Error-Handling/Error-Category-Codes) section.  In such case, you can refer to the returned error message to troubleshoot.   ## REST API Resource Codes  The 6-digit resource code indicates the REST API resource, typically a field of a Zuora object, on which the issue occurs. In the preceding example, `531003` refers to the `termType` field of the `subscription` object.   The value range for all REST API resource codes is from `500000` to `679999`. See <a href=\"https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Resource_Codes\" target=\"_blank\">Resource Codes</a> in the Knowledge Center for a full list of resource codes.  ## Error Category Codes  The 2-digit error category code identifies the type of error, for example, resource not found or missing required field.   The following table describes all error categories and the corresponding resolution:  | Code    | Error category              | Description    | Resolution    | |:--------|:--------|:--------|:--------| | 10      | Permission or access denied | The request cannot be processed because a certain tenant or user permission is missing. | Check the missing tenant or user permission in the response message and contact <a href=\"https://support.zuora.com\" target=\"_blank\">Zuora Global Support</a> for enablement. | | 11      | Authentication failed       | Authentication fails due to invalid API authentication credentials. | Ensure that a valid API credential is specified. | | 20      | Invalid format or value     | The request cannot be processed due to an invalid field format or value. | Check the invalid field in the error message, and ensure that the format and value of all fields you passed in are valid. | | 21      | Unknown field in request    | The request cannot be processed because an unknown field exists in the request body. | Check the unknown field name in the response message, and ensure that you do not include any unknown field in the request body. | | 22      | Missing required field      | The request cannot be processed because a required field in the request body is missing. | Check the missing field name in the response message, and ensure that you include all required fields in the request body. | | 23      | Missing required parameter  | The request cannot be processed because a required query parameter is missing. | Check the missing parameter name in the response message, and ensure that you include the parameter in the query. | | 30      | Rule restriction            | The request cannot be processed due to the violation of a Zuora business rule. | Check the response message and ensure that the API request meets the specified business rules. | | 40      | Not found                   | The specified resource cannot be found. | Check the response message and ensure that the specified resource exists in your Zuora tenant. | | 45      | Unsupported request         | The requested endpoint does not support the specified HTTP method. | Check your request and ensure that the endpoint and method matches. | | 50      | Locking contention          | This request cannot be processed because the objects this request is trying to modify are being modified by another API request, UI operation, or batch job process. | <p>Resubmit the request first to have another try.</p> <p>If this error still occurs, contact <a href=\"https://support.zuora.com\" target=\"_blank\">Zuora Global Support</a> with the returned `Zuora-Request-Id` value in the response header for assistance.</p> | | 60      | Internal error              | The server encounters an internal error. | Contact <a href=\"https://support.zuora.com\" target=\"_blank\">Zuora Global Support</a> with the returned `Zuora-Request-Id` value in the response header for assistance. | | 61      | Temporary error             | A temporary error occurs during request processing, for example, a database communication error. | <p>Resubmit the request first to have another try.</p> <p>If this error still occurs, contact <a href=\"https://support.zuora.com\" target=\"_blank\">Zuora Global Support</a> with the returned `Zuora-Request-Id` value in the response header for assistance. </p>| | 70      | Request exceeded limit      | The total number of concurrent requests exceeds the limit allowed by the system. | <p>Resubmit the request after the number of seconds specified by the `Retry-After` value in the response header.</p> <p>Check [Concurrent request limits](https://developer.zuora.com/rest-api/general-concepts/rate-concurrency-limits/) for details about Zuora’s concurrent request limit policy.</p> | | 90      | Malformed request           | The request cannot be processed due to JSON syntax errors. | Check the syntax error in the JSON request body and ensure that the request is in the correct JSON format. | | 99      | Integration error           | The server encounters an error when communicating with an external system, for example, payment gateway, tax engine provider. | Check the response message and take action accordingly. |   # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.   ## Major Version   The major version number of the REST API appears in the REST URL. In this API reference, only the **v1** major version is available. For example, `POST https://rest.zuora.com/v1/subscriptions`.       Zuora also offers the [Quickstart API](https://developer.zuora.com/quickstart-api/quickstart-api-introduction/) that uses the **v2** major version. For more information about which version to use, see [Which API Should I Use](https://developer.zuora.com/api-reference-guide/).   ## Minor Version   Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.    Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not consecutive.  You can use the following versions to override the default version (`186.0`):   - 187.0   - 188.0   - 189.0   - 196.0   - 206.0   - 207.0   - 211.0   - 214.0   - 215.0   - 216.0   - 223.0   - 224.0   - 230.0   - 239.0   - 256.0   - 257.0   - 309.0   - 314.0   - 315.0   - 329.0   - 330.0   - 336.0   - 337.0   - 338.0   - 341.0  If you set the `zuora-version` header to a version excluded from the preceding list, the corresponding API request is processed as you use the default version, `186.0`.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 206.0 and earlier  | [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 206.0 and earlier| [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 206.0 and earlier| [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://developer.zuora.com/api-references/api/operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://developer.zuora.com/api-references/api/operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://developer.zuora.com/api-references/api/operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://developer.zuora.com/api-references/api/operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://developer.zuora.com/api-references/api/operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://developer.zuora.com/api-references/api/operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. | | chargeId | 256.0 and earlier | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | productRatePlanChargeId | 257.0 and later | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | comment | 256.0 and earlier | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItem \"Get debit memo item\") | Comments about the product rate plan charge, invoice item, or memo item. | | description | 257.0 and later | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItem \"Get debit memo item\") | Description of the the product rate plan charge, invoice item, or memo item. | | taxationItems | 309.0 and later | [Preview an order](https://developer.zuora.com/api-references/api/operation/POST_PreviewOrder \"Preview an order\") | List of taxation items for an invoice item or a credit memo item. | | batch | 309.0 and earlier | [Create a billing preview run](https://developer.zuora.com/api-references/api/operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. |       | batches | 314.0 and later | [Create a billing preview run](https://developer.zuora.com/api-references/api/operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. | | taxationItems | 315.0 and later | [Preview a subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview a subscription\"); [Update a subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update a subscription\")| List of taxation items for an invoice item or a credit memo item. | | billingDocument | 330.0 and later | [Create a payment schedule](https://developer.zuora.com/api-references/api/operation/POST_PaymentSchedule \"Create a payment schedule\"); [Create multiple payment schedules at once](https://developer.zuora.com/api-references/api/operation/POST_PaymentSchedules \"Create multiple payment schedules at once\")| The billing document with which the payment schedule item is associated. | | paymentId | 336.0 and earlier | [Add payment schedule items to a custom payment schedule](https://developer.zuora.com/api-references/api/operation/POST_AddItemsToCustomPaymentSchedule/ \"Add payment schedule items to a custom payment schedule\"); [Update a payment schedule](https://developer.zuora.com/api-references/api/operation/PUT_PaymentSchedule/ \"Update a payment schedule\"); [Update a payment schedule item](https://developer.zuora.com/api-references/api/operation/PUT_PaymentScheduleItem/ \"Update a payment schedule item\"); [Preview the result of payment schedule update](https://developer.zuora.com/api-references/api/operation/PUT_PaymentScheduleUpdatePreview/ \"Preview the result of payment schedule update\"); [Retrieve a payment schedule](https://developer.zuora.com/api-references/api/operation/GET_PaymentSchedule/ \"Retrieve a payment schedule\"); [Retrieve a payment schedule item](https://developer.zuora.com/api-references/api/operation/GET_PaymentScheduleItem/ \"Retrieve a payment schedule item\"); [List payment schedules by customer account](https://developer.zuora.com/api-references/api/operation/GET_PaymentSchedules/ \"List payment schedules by customer account\"); [Cancel a payment schedule](https://developer.zuora.com/api-references/api/operation/PUT_CancelPaymentSchedule/ \"Cancel a payment schedule\"); [Cancel a payment schedule item](https://developer.zuora.com/api-references/api/operation/PUT_CancelPaymentScheduleItem/ \"Cancel a payment schedule item\");[Skip a payment schedule item](https://developer.zuora.com/api-references/api/operation/PUT_SkipPaymentScheduleItem/ \"Skip a payment schedule item\");[Retry failed payment schedule items](https://developer.zuora.com/api-references/api/operation/POST_RetryPaymentScheduleItem/ \"Retry failed payment schedule items\") | ID of the payment to be linked to the payment schedule item.   #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription) and [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics   # API Names for Zuora Objects  For information about the Zuora business object model, see [Zuora Business Object Model](https://developer.zuora.com/rest-api/general-concepts/object-model/).  You can use the [Describe](https://developer.zuora.com/api-references/api/operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun` - API name used  in the [Describe](https://developer.zuora.com/api-references/api/operation/GET_Describe) operation, Export ZOQL queries, and Data Query.</p> <p>`BillRun` - API name used in the [Actions](https://developer.zuora.com/api-references/api/tag/Actions). See the CRUD oprations of [Bill Run](https://developer.zuora.com/api-references/api/tag/Bill-Run) for more information about the `BillRun` object. `BillingRun` and `BillRun` have different fields. |                      | Billing Preview Run                           | `BillingPreviewRun`                        |                      | Configuration Templates                       | `ConfigurationTemplates`                   | | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Fulfillment                                   | `Fulfillment`                              | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Invoice Schedule                              | `InvoiceSchedule`                          | | Invoice Schedule Item                         | `InvoiceScheduleItem`                      | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Notification History - Callout                | `CalloutHistory`                           | | Notification History - Email                  | `EmailHistory`                             | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Line Items                              | `OrderLineItems`                           |     | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                        | `UpdaterDetail`                             | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Charge Definition                     | `ProductChargeDefinition`                  |     | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Definition                  | `ProductRatePlanDefinition`                |     | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    | 

    The version of the OpenAPI document: 2024-03-15
    Contact: docs@zuora.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from zuora_python_sdk import schemas  # noqa: F401


class GETProductChargeDefinitionsResponseChargeDefinitionsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            
            
            class applyDiscountTo(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ONETIME": "ONETIME",
                        "RECURRING": "RECURRING",
                        "USAGE": "USAGE",
                        "ONETIMERECURRING": "ONETIMERECURRING",
                        "ONETIMEUSAGE": "ONETIMEUSAGE",
                        "RECURRINGUSAGE": "RECURRINGUSAGE",
                        "ONETIMERECURRINGUSAGE": "ONETIMERECURRINGUSAGE",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def ONETIME(cls):
                    return cls("ONETIME")
                
                @schemas.classproperty
                def RECURRING(cls):
                    return cls("RECURRING")
                
                @schemas.classproperty
                def USAGE(cls):
                    return cls("USAGE")
                
                @schemas.classproperty
                def ONETIMERECURRING(cls):
                    return cls("ONETIMERECURRING")
                
                @schemas.classproperty
                def ONETIMEUSAGE(cls):
                    return cls("ONETIMEUSAGE")
                
                @schemas.classproperty
                def RECURRINGUSAGE(cls):
                    return cls("RECURRINGUSAGE")
                
                @schemas.classproperty
                def ONETIMERECURRINGUSAGE(cls):
                    return cls("ONETIMERECURRINGUSAGE")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'applyDiscountTo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            billingDay = schemas.StrSchema
            billingPeriod = schemas.StrSchema
            
            
            class billingPeriodAlignment(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALIGN_TO_CHARGE(cls):
                    return cls("AlignToCharge")
                
                @schemas.classproperty
                def ALIGN_TO_SUBSCRIPTION_START(cls):
                    return cls("AlignToSubscriptionStart")
                
                @schemas.classproperty
                def ALIGN_TO_TERM_START(cls):
                    return cls("AlignToTermStart")
                
                @schemas.classproperty
                def ALIGN_TO_TERM_END(cls):
                    return cls("AlignToTermEnd")
            
            
            class billingTiming(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ADVANCE(cls):
                    return cls("IN_ADVANCE")
                
                @schemas.classproperty
                def ARREARS(cls):
                    return cls("IN_ARREARS")
            
            
            class chargeModel(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DISCOUNT_FIXED_AMOUNT(cls):
                    return cls("DiscountFixedAmount")
                
                @schemas.classproperty
                def DISCOUNT_PERCENTAGE(cls):
                    return cls("DiscountPercentage")
                
                @schemas.classproperty
                def FLAT_FEE(cls):
                    return cls("FlatFee")
                
                @schemas.classproperty
                def PER_UNIT(cls):
                    return cls("PerUnit")
                
                @schemas.classproperty
                def OVERAGE(cls):
                    return cls("Overage")
                
                @schemas.classproperty
                def TIERED(cls):
                    return cls("Tiered")
                
                @schemas.classproperty
                def TIERED_WITH_OVERAGE(cls):
                    return cls("TieredWithOverage")
                
                @schemas.classproperty
                def VOLUME(cls):
                    return cls("Volume")
                
                @schemas.classproperty
                def DELIVERY(cls):
                    return cls("Delivery")
                
                @schemas.classproperty
                def MULTI_ATTRIBUTE_PRICING(cls):
                    return cls("MultiAttributePricing")
                
                @schemas.classproperty
                def PRERATED_PER_UNIT(cls):
                    return cls("PreratedPerUnit")
                
                @schemas.classproperty
                def PRERATED_PRICING(cls):
                    return cls("PreratedPricing")
                
                @schemas.classproperty
                def HIGH_WATERMARK_VOLUME_PRICING(cls):
                    return cls("HighWatermarkVolumePricing")
                
                @schemas.classproperty
                def HIGH_WATERMARK_TIERED_PRICING(cls):
                    return cls("HighWatermarkTieredPricing")
            
            
            class chargeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ONE_TIME(cls):
                    return cls("OneTime")
                
                @schemas.classproperty
                def RECURRING(cls):
                    return cls("Recurring")
                
                @schemas.classproperty
                def USAGE(cls):
                    return cls("Usage")
        
            @staticmethod
            def customFields() -> typing.Type['ProductChargeDefinitionObjectCustomFields']:
                return ProductChargeDefinitionObjectCustomFields
            
            
            class defaultQuantity(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'defaultQuantity':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def deliverySchedule() -> typing.Type['GETDeliverySchedule']:
                return GETDeliverySchedule
            
            
            class discountClass(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'discountClass':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class discountLevel(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "rateplan": "RATEPLAN",
                        "subscription": "SUBSCRIPTION",
                        "account": "ACCOUNT",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def RATEPLAN(cls):
                    return cls("rateplan")
                
                @schemas.classproperty
                def SUBSCRIPTION(cls):
                    return cls("subscription")
                
                @schemas.classproperty
                def ACCOUNT(cls):
                    return cls("account")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'discountLevel':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            effectiveEndDate = schemas.DateTimeSchema
            effectiveStartDate = schemas.DateTimeSchema
            
            
            class endDateCondition(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SUBSCRIPTION_END(cls):
                    return cls("Subscription_End")
                
                @schemas.classproperty
                def ONE_TIME(cls):
                    return cls("One_Time")
                
                @schemas.classproperty
                def FIXED_PERIOD(cls):
                    return cls("Fixed_Period")
                
                @schemas.classproperty
                def SPECIFIC_END_DATE(cls):
                    return cls("Specific_End_Date")
            excludeItemBillingFromRevenueAccounting = schemas.BoolSchema
            excludeItemBookingFromRevenueAccounting = schemas.BoolSchema
            isAllocationEligible = schemas.BoolSchema
            isUnbilled = schemas.BoolSchema
            productCategory = schemas.StrSchema
            productClass = schemas.StrSchema
            productFamily = schemas.StrSchema
            productLine = schemas.StrSchema
            
            
            class revenueRecognitionTiming(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BILLING_DOCUMENT_POSTING_DATE(cls):
                    return cls("Upon Billing Document Posting Date")
                
                @schemas.classproperty
                def ORDER_ACTIVATION_DATE(cls):
                    return cls("Upon Order Activation Date")
            
            
            class revenueAmortizationMethod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def IMMEDIATE(cls):
                    return cls("Immediate")
                
                @schemas.classproperty
                def RATABLE_USING_START_AND_END_DATES(cls):
                    return cls("Ratable Using Start And End Dates")
            
            
            class numberOfPeriods(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'numberOfPeriods':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def financeInformation() -> typing.Type['GETProductChargeDefinitionsResponseChargeDefinitionsItemFinanceInformation']:
                return GETProductChargeDefinitionsResponseChargeDefinitionsItemFinanceInformation
            isDefault = schemas.BoolSchema
            isStackedDiscount = schemas.BoolSchema
            
            
            class listPriceBase(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BILLING_PERIOD(cls):
                    return cls("Per_Billing_Period")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("Per_Month")
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("Per_Week")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("Per_Year")
            numberOfPeriod = schemas.Int64Schema
            
            
            class overageCalculationOption(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EndOfSmoothingPeriod": "END_OF_SMOOTHING_PERIOD",
                        "PerBillingPeriod": "PER_BILLING_PERIOD",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def END_OF_SMOOTHING_PERIOD(cls):
                    return cls("EndOfSmoothingPeriod")
                
                @schemas.classproperty
                def PER_BILLING_PERIOD(cls):
                    return cls("PerBillingPeriod")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'overageCalculationOption':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class overageUnusedUnitsCreditOption(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NoCredit": "NO_CREDIT",
                        "CreditBySpecificRate": "CREDIT_BY_SPECIFIC_RATE",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def NO_CREDIT(cls):
                    return cls("NoCredit")
                
                @schemas.classproperty
                def CREDIT_BY_SPECIFIC_RATE(cls):
                    return cls("CreditBySpecificRate")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'overageUnusedUnitsCreditOption':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class priceChangeOption(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NoChange": "NO_CHANGE",
                        "SpecificPercentageValue": "SPECIFIC_PERCENTAGE_VALUE",
                        "UseLatestProductCatalogPricing": "USE_LATEST_PRODUCT_CATALOG_PRICING",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def NO_CHANGE(cls):
                    return cls("NoChange")
                
                @schemas.classproperty
                def SPECIFIC_PERCENTAGE_VALUE(cls):
                    return cls("SpecificPercentageValue")
                
                @schemas.classproperty
                def USE_LATEST_PRODUCT_CATALOG_PRICING(cls):
                    return cls("UseLatestProductCatalogPricing")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'priceChangeOption':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class priceIncreaseOption(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FROM_TENANT_PERCENTAGE_VALUE(cls):
                    return cls("FromTenantPercentageValue")
                
                @schemas.classproperty
                def SPECIFIC_PERCENTAGE_VALUE(cls):
                    return cls("SpecificPercentageValue")
            
            
            class priceIncreasePercentage(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'priceIncreasePercentage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class prices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GETProductChargeDefinitionPricing']:
                        return GETProductChargeDefinitionPricing
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GETProductChargeDefinitionPricing'], typing.List['GETProductChargeDefinitionPricing']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'prices':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GETProductChargeDefinitionPricing':
                    return super().__getitem__(i)
            productChargeDefinitionId = schemas.StrSchema
            productChargeDefinitionNumber = schemas.StrSchema
            
            
            class productDiscountApplyDetails(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GETProductDiscountApplyDetailsType']:
                        return GETProductDiscountApplyDetailsType
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GETProductDiscountApplyDetailsType'], typing.List['GETProductDiscountApplyDetailsType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'productDiscountApplyDetails':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GETProductDiscountApplyDetailsType':
                    return super().__getitem__(i)
            productRatePlanChargeId = schemas.StrSchema
            
            
            class productRatePlanChargeNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'productRatePlanChargeNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class productRatePlanId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'productRatePlanId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class productRatePlanName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'productRatePlanName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class productRatePlanNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'productRatePlanNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ratingGroup(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ByBillingPeriod": "BY_BILLING_PERIOD",
                        "ByUsageStartDate": "BY_USAGE_START_DATE",
                        "ByUsageRecord": "BY_USAGE_RECORD",
                        "ByUsageUpload": "BY_USAGE_UPLOAD",
                        "ByGroupId": "BY_GROUP_ID",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def BY_BILLING_PERIOD(cls):
                    return cls("ByBillingPeriod")
                
                @schemas.classproperty
                def BY_USAGE_START_DATE(cls):
                    return cls("ByUsageStartDate")
                
                @schemas.classproperty
                def BY_USAGE_RECORD(cls):
                    return cls("ByUsageRecord")
                
                @schemas.classproperty
                def BY_USAGE_UPLOAD(cls):
                    return cls("ByUsageUpload")
                
                @schemas.classproperty
                def BY_GROUP_ID(cls):
                    return cls("ByGroupId")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ratingGroup':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class recognizedRevenueAccount(
                schemas.StrSchema
            ):
                pass
            
            
            class revRecCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'revRecCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class revRecTriggerCondition(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ContractEffectiveDate": "CONTRACT_EFFECTIVE_DATE",
                        "ServiceActivationDate": "SERVICE_ACTIVATION_DATE",
                        "CustomerAcceptanceDate": "CUSTOMER_ACCEPTANCE_DATE",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def CONTRACT_EFFECTIVE_DATE(cls):
                    return cls("ContractEffectiveDate")
                
                @schemas.classproperty
                def SERVICE_ACTIVATION_DATE(cls):
                    return cls("ServiceActivationDate")
                
                @schemas.classproperty
                def CUSTOMER_ACCEPTANCE_DATE(cls):
                    return cls("CustomerAcceptanceDate")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'revRecTriggerCondition':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class revenueRecognitionRuleName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UPON_INVOICING(cls):
                    return cls("Recognize upon invoicing")
                
                @schemas.classproperty
                def DAILY_OVER_TIME(cls):
                    return cls("Recognize daily over time")
            
            
            class smoothingModel(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "RollingWindow": "ROLLING_WINDOW",
                        "Rollover": "ROLLOVER",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def ROLLING_WINDOW(cls):
                    return cls("RollingWindow")
                
                @schemas.classproperty
                def ROLLOVER(cls):
                    return cls("Rollover")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'smoothingModel':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class specificBillingPeriod(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'specificBillingPeriod':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class specificListPriceBase(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'specificListPriceBase':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class taxCode(
                schemas.StrSchema
            ):
                pass
            
            
            class taxMode(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "TaxExclusive": "TAX_EXCLUSIVE",
                        "TaxInclusive": "TAX_INCLUSIVE",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def TAX_EXCLUSIVE(cls):
                    return cls("TaxExclusive")
                
                @schemas.classproperty
                def TAX_INCLUSIVE(cls):
                    return cls("TaxInclusive")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'taxMode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            taxable = schemas.BoolSchema
            
            
            class term(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'term':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class termPeriodType(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Month": "MONTH",
                        "Year": "YEAR",
                        "Day": "DAY",
                        "Week": "WEEK",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("Month")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("Year")
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("Day")
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("Week")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'termPeriodType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class termType(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "TERMED": "TERMED",
                        "EVERGREEN": "EVERGREEN",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def TERMED(cls):
                    return cls("TERMED")
                
                @schemas.classproperty
                def EVERGREEN(cls):
                    return cls("EVERGREEN")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'termType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class triggerEvent(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CONTRACT_EFFECTIVE(cls):
                    return cls("ContractEffective")
                
                @schemas.classproperty
                def SERVICE_ACTIVATION(cls):
                    return cls("ServiceActivation")
                
                @schemas.classproperty
                def CUSTOMER_ACCEPTANCE(cls):
                    return cls("CustomerAcceptance")
            
            
            class uom(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'uom':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class upToPeriods(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'upToPeriods':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class upToPeriodsType(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Billing_Periods": "BILLING_PERIODS",
                        "Days": "DAYS",
                        "Weeks": "WEEKS",
                        "Months": "MONTHS",
                        "Years": "YEARS",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def BILLING_PERIODS(cls):
                    return cls("Billing_Periods")
                
                @schemas.classproperty
                def DAYS(cls):
                    return cls("Days")
                
                @schemas.classproperty
                def WEEKS(cls):
                    return cls("Weeks")
                
                @schemas.classproperty
                def MONTHS(cls):
                    return cls("Months")
                
                @schemas.classproperty
                def YEARS(cls):
                    return cls("Years")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'upToPeriodsType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class usageRecordRatingOption(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EndOfBillingPeriod": "END_OF_BILLING_PERIOD",
                        "OnDemand": "ON_DEMAND",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def END_OF_BILLING_PERIOD(cls):
                    return cls("EndOfBillingPeriod")
                
                @schemas.classproperty
                def ON_DEMAND(cls):
                    return cls("OnDemand")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'usageRecordRatingOption':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class useDiscountSpecificAccountingCode(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'useDiscountSpecificAccountingCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            useTenantDefaultForPriceChange = schemas.BoolSchema
            __annotations__ = {
                "description": description,
                "applyDiscountTo": applyDiscountTo,
                "billingDay": billingDay,
                "billingPeriod": billingPeriod,
                "billingPeriodAlignment": billingPeriodAlignment,
                "billingTiming": billingTiming,
                "chargeModel": chargeModel,
                "chargeType": chargeType,
                "customFields": customFields,
                "defaultQuantity": defaultQuantity,
                "deliverySchedule": deliverySchedule,
                "discountClass": discountClass,
                "discountLevel": discountLevel,
                "effectiveEndDate": effectiveEndDate,
                "effectiveStartDate": effectiveStartDate,
                "endDateCondition": endDateCondition,
                "excludeItemBillingFromRevenueAccounting": excludeItemBillingFromRevenueAccounting,
                "excludeItemBookingFromRevenueAccounting": excludeItemBookingFromRevenueAccounting,
                "isAllocationEligible": isAllocationEligible,
                "isUnbilled": isUnbilled,
                "productCategory": productCategory,
                "productClass": productClass,
                "productFamily": productFamily,
                "productLine": productLine,
                "revenueRecognitionTiming": revenueRecognitionTiming,
                "revenueAmortizationMethod": revenueAmortizationMethod,
                "numberOfPeriods": numberOfPeriods,
                "financeInformation": financeInformation,
                "isDefault": isDefault,
                "isStackedDiscount": isStackedDiscount,
                "listPriceBase": listPriceBase,
                "numberOfPeriod": numberOfPeriod,
                "overageCalculationOption": overageCalculationOption,
                "overageUnusedUnitsCreditOption": overageUnusedUnitsCreditOption,
                "priceChangeOption": priceChangeOption,
                "priceIncreaseOption": priceIncreaseOption,
                "priceIncreasePercentage": priceIncreasePercentage,
                "prices": prices,
                "productChargeDefinitionId": productChargeDefinitionId,
                "productChargeDefinitionNumber": productChargeDefinitionNumber,
                "productDiscountApplyDetails": productDiscountApplyDetails,
                "productRatePlanChargeId": productRatePlanChargeId,
                "productRatePlanChargeNumber": productRatePlanChargeNumber,
                "productRatePlanId": productRatePlanId,
                "productRatePlanName": productRatePlanName,
                "productRatePlanNumber": productRatePlanNumber,
                "ratingGroup": ratingGroup,
                "recognizedRevenueAccount": recognizedRevenueAccount,
                "revRecCode": revRecCode,
                "revRecTriggerCondition": revRecTriggerCondition,
                "revenueRecognitionRuleName": revenueRecognitionRuleName,
                "smoothingModel": smoothingModel,
                "specificBillingPeriod": specificBillingPeriod,
                "specificListPriceBase": specificListPriceBase,
                "taxCode": taxCode,
                "taxMode": taxMode,
                "taxable": taxable,
                "term": term,
                "termPeriodType": termPeriodType,
                "termType": termType,
                "triggerEvent": triggerEvent,
                "uom": uom,
                "upToPeriods": upToPeriods,
                "upToPeriodsType": upToPeriodsType,
                "usageRecordRatingOption": usageRecordRatingOption,
                "useDiscountSpecificAccountingCode": useDiscountSpecificAccountingCode,
                "useTenantDefaultForPriceChange": useTenantDefaultForPriceChange,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applyDiscountTo"]) -> MetaOapg.properties.applyDiscountTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingDay"]) -> MetaOapg.properties.billingDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingPeriod"]) -> MetaOapg.properties.billingPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingPeriodAlignment"]) -> MetaOapg.properties.billingPeriodAlignment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingTiming"]) -> MetaOapg.properties.billingTiming: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeModel"]) -> MetaOapg.properties.chargeModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeType"]) -> MetaOapg.properties.chargeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> 'ProductChargeDefinitionObjectCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultQuantity"]) -> MetaOapg.properties.defaultQuantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deliverySchedule"]) -> 'GETDeliverySchedule': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discountClass"]) -> MetaOapg.properties.discountClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discountLevel"]) -> MetaOapg.properties.discountLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveEndDate"]) -> MetaOapg.properties.effectiveEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveStartDate"]) -> MetaOapg.properties.effectiveStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDateCondition"]) -> MetaOapg.properties.endDateCondition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excludeItemBillingFromRevenueAccounting"]) -> MetaOapg.properties.excludeItemBillingFromRevenueAccounting: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excludeItemBookingFromRevenueAccounting"]) -> MetaOapg.properties.excludeItemBookingFromRevenueAccounting: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAllocationEligible"]) -> MetaOapg.properties.isAllocationEligible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isUnbilled"]) -> MetaOapg.properties.isUnbilled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productCategory"]) -> MetaOapg.properties.productCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productClass"]) -> MetaOapg.properties.productClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productFamily"]) -> MetaOapg.properties.productFamily: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productLine"]) -> MetaOapg.properties.productLine: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenueRecognitionTiming"]) -> MetaOapg.properties.revenueRecognitionTiming: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenueAmortizationMethod"]) -> MetaOapg.properties.revenueAmortizationMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfPeriods"]) -> MetaOapg.properties.numberOfPeriods: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["financeInformation"]) -> 'GETProductChargeDefinitionsResponseChargeDefinitionsItemFinanceInformation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isStackedDiscount"]) -> MetaOapg.properties.isStackedDiscount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["listPriceBase"]) -> MetaOapg.properties.listPriceBase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfPeriod"]) -> MetaOapg.properties.numberOfPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overageCalculationOption"]) -> MetaOapg.properties.overageCalculationOption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overageUnusedUnitsCreditOption"]) -> MetaOapg.properties.overageUnusedUnitsCreditOption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priceChangeOption"]) -> MetaOapg.properties.priceChangeOption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priceIncreaseOption"]) -> MetaOapg.properties.priceIncreaseOption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priceIncreasePercentage"]) -> MetaOapg.properties.priceIncreasePercentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prices"]) -> MetaOapg.properties.prices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productChargeDefinitionId"]) -> MetaOapg.properties.productChargeDefinitionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productChargeDefinitionNumber"]) -> MetaOapg.properties.productChargeDefinitionNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productDiscountApplyDetails"]) -> MetaOapg.properties.productDiscountApplyDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productRatePlanChargeId"]) -> MetaOapg.properties.productRatePlanChargeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productRatePlanChargeNumber"]) -> MetaOapg.properties.productRatePlanChargeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productRatePlanId"]) -> MetaOapg.properties.productRatePlanId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productRatePlanName"]) -> MetaOapg.properties.productRatePlanName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productRatePlanNumber"]) -> MetaOapg.properties.productRatePlanNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ratingGroup"]) -> MetaOapg.properties.ratingGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recognizedRevenueAccount"]) -> MetaOapg.properties.recognizedRevenueAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revRecCode"]) -> MetaOapg.properties.revRecCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revRecTriggerCondition"]) -> MetaOapg.properties.revRecTriggerCondition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenueRecognitionRuleName"]) -> MetaOapg.properties.revenueRecognitionRuleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smoothingModel"]) -> MetaOapg.properties.smoothingModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["specificBillingPeriod"]) -> MetaOapg.properties.specificBillingPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["specificListPriceBase"]) -> MetaOapg.properties.specificListPriceBase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCode"]) -> MetaOapg.properties.taxCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxMode"]) -> MetaOapg.properties.taxMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxable"]) -> MetaOapg.properties.taxable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["term"]) -> MetaOapg.properties.term: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["termPeriodType"]) -> MetaOapg.properties.termPeriodType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["termType"]) -> MetaOapg.properties.termType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["triggerEvent"]) -> MetaOapg.properties.triggerEvent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uom"]) -> MetaOapg.properties.uom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upToPeriods"]) -> MetaOapg.properties.upToPeriods: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upToPeriodsType"]) -> MetaOapg.properties.upToPeriodsType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usageRecordRatingOption"]) -> MetaOapg.properties.usageRecordRatingOption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useDiscountSpecificAccountingCode"]) -> MetaOapg.properties.useDiscountSpecificAccountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useTenantDefaultForPriceChange"]) -> MetaOapg.properties.useTenantDefaultForPriceChange: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "applyDiscountTo", "billingDay", "billingPeriod", "billingPeriodAlignment", "billingTiming", "chargeModel", "chargeType", "customFields", "defaultQuantity", "deliverySchedule", "discountClass", "discountLevel", "effectiveEndDate", "effectiveStartDate", "endDateCondition", "excludeItemBillingFromRevenueAccounting", "excludeItemBookingFromRevenueAccounting", "isAllocationEligible", "isUnbilled", "productCategory", "productClass", "productFamily", "productLine", "revenueRecognitionTiming", "revenueAmortizationMethod", "numberOfPeriods", "financeInformation", "isDefault", "isStackedDiscount", "listPriceBase", "numberOfPeriod", "overageCalculationOption", "overageUnusedUnitsCreditOption", "priceChangeOption", "priceIncreaseOption", "priceIncreasePercentage", "prices", "productChargeDefinitionId", "productChargeDefinitionNumber", "productDiscountApplyDetails", "productRatePlanChargeId", "productRatePlanChargeNumber", "productRatePlanId", "productRatePlanName", "productRatePlanNumber", "ratingGroup", "recognizedRevenueAccount", "revRecCode", "revRecTriggerCondition", "revenueRecognitionRuleName", "smoothingModel", "specificBillingPeriod", "specificListPriceBase", "taxCode", "taxMode", "taxable", "term", "termPeriodType", "termType", "triggerEvent", "uom", "upToPeriods", "upToPeriodsType", "usageRecordRatingOption", "useDiscountSpecificAccountingCode", "useTenantDefaultForPriceChange", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applyDiscountTo"]) -> typing.Union[MetaOapg.properties.applyDiscountTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingDay"]) -> typing.Union[MetaOapg.properties.billingDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingPeriod"]) -> typing.Union[MetaOapg.properties.billingPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingPeriodAlignment"]) -> typing.Union[MetaOapg.properties.billingPeriodAlignment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingTiming"]) -> typing.Union[MetaOapg.properties.billingTiming, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeModel"]) -> typing.Union[MetaOapg.properties.chargeModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeType"]) -> typing.Union[MetaOapg.properties.chargeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union['ProductChargeDefinitionObjectCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultQuantity"]) -> typing.Union[MetaOapg.properties.defaultQuantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deliverySchedule"]) -> typing.Union['GETDeliverySchedule', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discountClass"]) -> typing.Union[MetaOapg.properties.discountClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discountLevel"]) -> typing.Union[MetaOapg.properties.discountLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveEndDate"]) -> typing.Union[MetaOapg.properties.effectiveEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveStartDate"]) -> typing.Union[MetaOapg.properties.effectiveStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDateCondition"]) -> typing.Union[MetaOapg.properties.endDateCondition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excludeItemBillingFromRevenueAccounting"]) -> typing.Union[MetaOapg.properties.excludeItemBillingFromRevenueAccounting, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excludeItemBookingFromRevenueAccounting"]) -> typing.Union[MetaOapg.properties.excludeItemBookingFromRevenueAccounting, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAllocationEligible"]) -> typing.Union[MetaOapg.properties.isAllocationEligible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isUnbilled"]) -> typing.Union[MetaOapg.properties.isUnbilled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productCategory"]) -> typing.Union[MetaOapg.properties.productCategory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productClass"]) -> typing.Union[MetaOapg.properties.productClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productFamily"]) -> typing.Union[MetaOapg.properties.productFamily, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productLine"]) -> typing.Union[MetaOapg.properties.productLine, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenueRecognitionTiming"]) -> typing.Union[MetaOapg.properties.revenueRecognitionTiming, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenueAmortizationMethod"]) -> typing.Union[MetaOapg.properties.revenueAmortizationMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfPeriods"]) -> typing.Union[MetaOapg.properties.numberOfPeriods, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["financeInformation"]) -> typing.Union['GETProductChargeDefinitionsResponseChargeDefinitionsItemFinanceInformation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> typing.Union[MetaOapg.properties.isDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isStackedDiscount"]) -> typing.Union[MetaOapg.properties.isStackedDiscount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["listPriceBase"]) -> typing.Union[MetaOapg.properties.listPriceBase, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfPeriod"]) -> typing.Union[MetaOapg.properties.numberOfPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overageCalculationOption"]) -> typing.Union[MetaOapg.properties.overageCalculationOption, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overageUnusedUnitsCreditOption"]) -> typing.Union[MetaOapg.properties.overageUnusedUnitsCreditOption, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priceChangeOption"]) -> typing.Union[MetaOapg.properties.priceChangeOption, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priceIncreaseOption"]) -> typing.Union[MetaOapg.properties.priceIncreaseOption, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priceIncreasePercentage"]) -> typing.Union[MetaOapg.properties.priceIncreasePercentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prices"]) -> typing.Union[MetaOapg.properties.prices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productChargeDefinitionId"]) -> typing.Union[MetaOapg.properties.productChargeDefinitionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productChargeDefinitionNumber"]) -> typing.Union[MetaOapg.properties.productChargeDefinitionNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productDiscountApplyDetails"]) -> typing.Union[MetaOapg.properties.productDiscountApplyDetails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productRatePlanChargeId"]) -> typing.Union[MetaOapg.properties.productRatePlanChargeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productRatePlanChargeNumber"]) -> typing.Union[MetaOapg.properties.productRatePlanChargeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productRatePlanId"]) -> typing.Union[MetaOapg.properties.productRatePlanId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productRatePlanName"]) -> typing.Union[MetaOapg.properties.productRatePlanName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productRatePlanNumber"]) -> typing.Union[MetaOapg.properties.productRatePlanNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ratingGroup"]) -> typing.Union[MetaOapg.properties.ratingGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recognizedRevenueAccount"]) -> typing.Union[MetaOapg.properties.recognizedRevenueAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revRecCode"]) -> typing.Union[MetaOapg.properties.revRecCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revRecTriggerCondition"]) -> typing.Union[MetaOapg.properties.revRecTriggerCondition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenueRecognitionRuleName"]) -> typing.Union[MetaOapg.properties.revenueRecognitionRuleName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smoothingModel"]) -> typing.Union[MetaOapg.properties.smoothingModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["specificBillingPeriod"]) -> typing.Union[MetaOapg.properties.specificBillingPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["specificListPriceBase"]) -> typing.Union[MetaOapg.properties.specificListPriceBase, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCode"]) -> typing.Union[MetaOapg.properties.taxCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxMode"]) -> typing.Union[MetaOapg.properties.taxMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxable"]) -> typing.Union[MetaOapg.properties.taxable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["term"]) -> typing.Union[MetaOapg.properties.term, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["termPeriodType"]) -> typing.Union[MetaOapg.properties.termPeriodType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["termType"]) -> typing.Union[MetaOapg.properties.termType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["triggerEvent"]) -> typing.Union[MetaOapg.properties.triggerEvent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uom"]) -> typing.Union[MetaOapg.properties.uom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upToPeriods"]) -> typing.Union[MetaOapg.properties.upToPeriods, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upToPeriodsType"]) -> typing.Union[MetaOapg.properties.upToPeriodsType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usageRecordRatingOption"]) -> typing.Union[MetaOapg.properties.usageRecordRatingOption, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useDiscountSpecificAccountingCode"]) -> typing.Union[MetaOapg.properties.useDiscountSpecificAccountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useTenantDefaultForPriceChange"]) -> typing.Union[MetaOapg.properties.useTenantDefaultForPriceChange, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "applyDiscountTo", "billingDay", "billingPeriod", "billingPeriodAlignment", "billingTiming", "chargeModel", "chargeType", "customFields", "defaultQuantity", "deliverySchedule", "discountClass", "discountLevel", "effectiveEndDate", "effectiveStartDate", "endDateCondition", "excludeItemBillingFromRevenueAccounting", "excludeItemBookingFromRevenueAccounting", "isAllocationEligible", "isUnbilled", "productCategory", "productClass", "productFamily", "productLine", "revenueRecognitionTiming", "revenueAmortizationMethod", "numberOfPeriods", "financeInformation", "isDefault", "isStackedDiscount", "listPriceBase", "numberOfPeriod", "overageCalculationOption", "overageUnusedUnitsCreditOption", "priceChangeOption", "priceIncreaseOption", "priceIncreasePercentage", "prices", "productChargeDefinitionId", "productChargeDefinitionNumber", "productDiscountApplyDetails", "productRatePlanChargeId", "productRatePlanChargeNumber", "productRatePlanId", "productRatePlanName", "productRatePlanNumber", "ratingGroup", "recognizedRevenueAccount", "revRecCode", "revRecTriggerCondition", "revenueRecognitionRuleName", "smoothingModel", "specificBillingPeriod", "specificListPriceBase", "taxCode", "taxMode", "taxable", "term", "termPeriodType", "termType", "triggerEvent", "uom", "upToPeriods", "upToPeriodsType", "usageRecordRatingOption", "useDiscountSpecificAccountingCode", "useTenantDefaultForPriceChange", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        applyDiscountTo: typing.Union[MetaOapg.properties.applyDiscountTo, None, str, schemas.Unset] = schemas.unset,
        billingDay: typing.Union[MetaOapg.properties.billingDay, str, schemas.Unset] = schemas.unset,
        billingPeriod: typing.Union[MetaOapg.properties.billingPeriod, str, schemas.Unset] = schemas.unset,
        billingPeriodAlignment: typing.Union[MetaOapg.properties.billingPeriodAlignment, str, schemas.Unset] = schemas.unset,
        billingTiming: typing.Union[MetaOapg.properties.billingTiming, str, schemas.Unset] = schemas.unset,
        chargeModel: typing.Union[MetaOapg.properties.chargeModel, str, schemas.Unset] = schemas.unset,
        chargeType: typing.Union[MetaOapg.properties.chargeType, str, schemas.Unset] = schemas.unset,
        customFields: typing.Union['ProductChargeDefinitionObjectCustomFields', schemas.Unset] = schemas.unset,
        defaultQuantity: typing.Union[MetaOapg.properties.defaultQuantity, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        deliverySchedule: typing.Union['GETDeliverySchedule', schemas.Unset] = schemas.unset,
        discountClass: typing.Union[MetaOapg.properties.discountClass, None, str, schemas.Unset] = schemas.unset,
        discountLevel: typing.Union[MetaOapg.properties.discountLevel, None, str, schemas.Unset] = schemas.unset,
        effectiveEndDate: typing.Union[MetaOapg.properties.effectiveEndDate, str, datetime, schemas.Unset] = schemas.unset,
        effectiveStartDate: typing.Union[MetaOapg.properties.effectiveStartDate, str, datetime, schemas.Unset] = schemas.unset,
        endDateCondition: typing.Union[MetaOapg.properties.endDateCondition, str, schemas.Unset] = schemas.unset,
        excludeItemBillingFromRevenueAccounting: typing.Union[MetaOapg.properties.excludeItemBillingFromRevenueAccounting, bool, schemas.Unset] = schemas.unset,
        excludeItemBookingFromRevenueAccounting: typing.Union[MetaOapg.properties.excludeItemBookingFromRevenueAccounting, bool, schemas.Unset] = schemas.unset,
        isAllocationEligible: typing.Union[MetaOapg.properties.isAllocationEligible, bool, schemas.Unset] = schemas.unset,
        isUnbilled: typing.Union[MetaOapg.properties.isUnbilled, bool, schemas.Unset] = schemas.unset,
        productCategory: typing.Union[MetaOapg.properties.productCategory, str, schemas.Unset] = schemas.unset,
        productClass: typing.Union[MetaOapg.properties.productClass, str, schemas.Unset] = schemas.unset,
        productFamily: typing.Union[MetaOapg.properties.productFamily, str, schemas.Unset] = schemas.unset,
        productLine: typing.Union[MetaOapg.properties.productLine, str, schemas.Unset] = schemas.unset,
        revenueRecognitionTiming: typing.Union[MetaOapg.properties.revenueRecognitionTiming, str, schemas.Unset] = schemas.unset,
        revenueAmortizationMethod: typing.Union[MetaOapg.properties.revenueAmortizationMethod, str, schemas.Unset] = schemas.unset,
        numberOfPeriods: typing.Union[MetaOapg.properties.numberOfPeriods, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        financeInformation: typing.Union['GETProductChargeDefinitionsResponseChargeDefinitionsItemFinanceInformation', schemas.Unset] = schemas.unset,
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, schemas.Unset] = schemas.unset,
        isStackedDiscount: typing.Union[MetaOapg.properties.isStackedDiscount, bool, schemas.Unset] = schemas.unset,
        listPriceBase: typing.Union[MetaOapg.properties.listPriceBase, str, schemas.Unset] = schemas.unset,
        numberOfPeriod: typing.Union[MetaOapg.properties.numberOfPeriod, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        overageCalculationOption: typing.Union[MetaOapg.properties.overageCalculationOption, None, str, schemas.Unset] = schemas.unset,
        overageUnusedUnitsCreditOption: typing.Union[MetaOapg.properties.overageUnusedUnitsCreditOption, None, str, schemas.Unset] = schemas.unset,
        priceChangeOption: typing.Union[MetaOapg.properties.priceChangeOption, None, str, schemas.Unset] = schemas.unset,
        priceIncreaseOption: typing.Union[MetaOapg.properties.priceIncreaseOption, str, schemas.Unset] = schemas.unset,
        priceIncreasePercentage: typing.Union[MetaOapg.properties.priceIncreasePercentage, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        prices: typing.Union[MetaOapg.properties.prices, list, tuple, schemas.Unset] = schemas.unset,
        productChargeDefinitionId: typing.Union[MetaOapg.properties.productChargeDefinitionId, str, schemas.Unset] = schemas.unset,
        productChargeDefinitionNumber: typing.Union[MetaOapg.properties.productChargeDefinitionNumber, str, schemas.Unset] = schemas.unset,
        productDiscountApplyDetails: typing.Union[MetaOapg.properties.productDiscountApplyDetails, list, tuple, schemas.Unset] = schemas.unset,
        productRatePlanChargeId: typing.Union[MetaOapg.properties.productRatePlanChargeId, str, schemas.Unset] = schemas.unset,
        productRatePlanChargeNumber: typing.Union[MetaOapg.properties.productRatePlanChargeNumber, None, str, schemas.Unset] = schemas.unset,
        productRatePlanId: typing.Union[MetaOapg.properties.productRatePlanId, None, str, schemas.Unset] = schemas.unset,
        productRatePlanName: typing.Union[MetaOapg.properties.productRatePlanName, None, str, schemas.Unset] = schemas.unset,
        productRatePlanNumber: typing.Union[MetaOapg.properties.productRatePlanNumber, None, str, schemas.Unset] = schemas.unset,
        ratingGroup: typing.Union[MetaOapg.properties.ratingGroup, None, str, schemas.Unset] = schemas.unset,
        recognizedRevenueAccount: typing.Union[MetaOapg.properties.recognizedRevenueAccount, str, schemas.Unset] = schemas.unset,
        revRecCode: typing.Union[MetaOapg.properties.revRecCode, None, str, schemas.Unset] = schemas.unset,
        revRecTriggerCondition: typing.Union[MetaOapg.properties.revRecTriggerCondition, None, str, schemas.Unset] = schemas.unset,
        revenueRecognitionRuleName: typing.Union[MetaOapg.properties.revenueRecognitionRuleName, str, schemas.Unset] = schemas.unset,
        smoothingModel: typing.Union[MetaOapg.properties.smoothingModel, None, str, schemas.Unset] = schemas.unset,
        specificBillingPeriod: typing.Union[MetaOapg.properties.specificBillingPeriod, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        specificListPriceBase: typing.Union[MetaOapg.properties.specificListPriceBase, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        taxCode: typing.Union[MetaOapg.properties.taxCode, str, schemas.Unset] = schemas.unset,
        taxMode: typing.Union[MetaOapg.properties.taxMode, None, str, schemas.Unset] = schemas.unset,
        taxable: typing.Union[MetaOapg.properties.taxable, bool, schemas.Unset] = schemas.unset,
        term: typing.Union[MetaOapg.properties.term, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        termPeriodType: typing.Union[MetaOapg.properties.termPeriodType, None, str, schemas.Unset] = schemas.unset,
        termType: typing.Union[MetaOapg.properties.termType, None, str, schemas.Unset] = schemas.unset,
        triggerEvent: typing.Union[MetaOapg.properties.triggerEvent, str, schemas.Unset] = schemas.unset,
        uom: typing.Union[MetaOapg.properties.uom, None, str, schemas.Unset] = schemas.unset,
        upToPeriods: typing.Union[MetaOapg.properties.upToPeriods, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        upToPeriodsType: typing.Union[MetaOapg.properties.upToPeriodsType, None, str, schemas.Unset] = schemas.unset,
        usageRecordRatingOption: typing.Union[MetaOapg.properties.usageRecordRatingOption, None, str, schemas.Unset] = schemas.unset,
        useDiscountSpecificAccountingCode: typing.Union[MetaOapg.properties.useDiscountSpecificAccountingCode, None, bool, schemas.Unset] = schemas.unset,
        useTenantDefaultForPriceChange: typing.Union[MetaOapg.properties.useTenantDefaultForPriceChange, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GETProductChargeDefinitionsResponseChargeDefinitionsItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            applyDiscountTo=applyDiscountTo,
            billingDay=billingDay,
            billingPeriod=billingPeriod,
            billingPeriodAlignment=billingPeriodAlignment,
            billingTiming=billingTiming,
            chargeModel=chargeModel,
            chargeType=chargeType,
            customFields=customFields,
            defaultQuantity=defaultQuantity,
            deliverySchedule=deliverySchedule,
            discountClass=discountClass,
            discountLevel=discountLevel,
            effectiveEndDate=effectiveEndDate,
            effectiveStartDate=effectiveStartDate,
            endDateCondition=endDateCondition,
            excludeItemBillingFromRevenueAccounting=excludeItemBillingFromRevenueAccounting,
            excludeItemBookingFromRevenueAccounting=excludeItemBookingFromRevenueAccounting,
            isAllocationEligible=isAllocationEligible,
            isUnbilled=isUnbilled,
            productCategory=productCategory,
            productClass=productClass,
            productFamily=productFamily,
            productLine=productLine,
            revenueRecognitionTiming=revenueRecognitionTiming,
            revenueAmortizationMethod=revenueAmortizationMethod,
            numberOfPeriods=numberOfPeriods,
            financeInformation=financeInformation,
            isDefault=isDefault,
            isStackedDiscount=isStackedDiscount,
            listPriceBase=listPriceBase,
            numberOfPeriod=numberOfPeriod,
            overageCalculationOption=overageCalculationOption,
            overageUnusedUnitsCreditOption=overageUnusedUnitsCreditOption,
            priceChangeOption=priceChangeOption,
            priceIncreaseOption=priceIncreaseOption,
            priceIncreasePercentage=priceIncreasePercentage,
            prices=prices,
            productChargeDefinitionId=productChargeDefinitionId,
            productChargeDefinitionNumber=productChargeDefinitionNumber,
            productDiscountApplyDetails=productDiscountApplyDetails,
            productRatePlanChargeId=productRatePlanChargeId,
            productRatePlanChargeNumber=productRatePlanChargeNumber,
            productRatePlanId=productRatePlanId,
            productRatePlanName=productRatePlanName,
            productRatePlanNumber=productRatePlanNumber,
            ratingGroup=ratingGroup,
            recognizedRevenueAccount=recognizedRevenueAccount,
            revRecCode=revRecCode,
            revRecTriggerCondition=revRecTriggerCondition,
            revenueRecognitionRuleName=revenueRecognitionRuleName,
            smoothingModel=smoothingModel,
            specificBillingPeriod=specificBillingPeriod,
            specificListPriceBase=specificListPriceBase,
            taxCode=taxCode,
            taxMode=taxMode,
            taxable=taxable,
            term=term,
            termPeriodType=termPeriodType,
            termType=termType,
            triggerEvent=triggerEvent,
            uom=uom,
            upToPeriods=upToPeriods,
            upToPeriodsType=upToPeriodsType,
            usageRecordRatingOption=usageRecordRatingOption,
            useDiscountSpecificAccountingCode=useDiscountSpecificAccountingCode,
            useTenantDefaultForPriceChange=useTenantDefaultForPriceChange,
            _configuration=_configuration,
            **kwargs,
        )

from zuora_python_sdk.model.get_delivery_schedule import GETDeliverySchedule
from zuora_python_sdk.model.get_product_charge_definition_pricing import GETProductChargeDefinitionPricing
from zuora_python_sdk.model.get_product_charge_definitions_response_charge_definitions_item_finance_information import GETProductChargeDefinitionsResponseChargeDefinitionsItemFinanceInformation
from zuora_python_sdk.model.get_product_discount_apply_details_type import GETProductDiscountApplyDetailsType
from zuora_python_sdk.model.product_charge_definition_object_custom_fields import ProductChargeDefinitionObjectCustomFields

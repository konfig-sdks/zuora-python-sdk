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


class GETSubscriptionTypeWithSuccess(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    version = schemas.Int64Schema
                    accountId = schemas.StrSchema
                    accountName = schemas.StrSchema
                    accountNumber = schemas.StrSchema
                    autoRenew = schemas.BoolSchema
                
                    @staticmethod
                    def billToContact() -> typing.Type['GETAccountSummaryTypeBillToContact']:
                        return GETAccountSummaryTypeBillToContact
                    cancelReason = schemas.StrSchema
                    contractEffectiveDate = schemas.DateSchema
                    contractedMrr = schemas.NumberSchema
                    currency = schemas.StrSchema
                    currentTerm = schemas.Int64Schema
                    currentTermPeriodType = schemas.StrSchema
                    customerAcceptanceDate = schemas.DateSchema
                    
                    
                    class externallyManagedBy(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "Amazon": "AMAZON",
                                "Apple": "APPLE",
                                "Google": "GOOGLE",
                                "Roku": "ROKU",
                            }
                        
                        @schemas.classproperty
                        def AMAZON(cls):
                            return cls("Amazon")
                        
                        @schemas.classproperty
                        def APPLE(cls):
                            return cls("Apple")
                        
                        @schemas.classproperty
                        def GOOGLE(cls):
                            return cls("Google")
                        
                        @schemas.classproperty
                        def ROKU(cls):
                            return cls("Roku")
                    id = schemas.StrSchema
                    initialTerm = schemas.Int64Schema
                    initialTermPeriodType = schemas.StrSchema
                    
                    
                    class invoiceGroupNumber(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'invoiceGroupNumber':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    invoiceOwnerAccountId = schemas.StrSchema
                    invoiceOwnerAccountName = schemas.StrSchema
                    invoiceOwnerAccountNumber = schemas.StrSchema
                    invoiceScheduleId = schemas.IntSchema
                    invoiceSeparately = schemas.StrSchema
                    invoiceTemplateId = schemas.StrSchema
                    invoiceTemplateName = schemas.StrSchema
                    isLatestVersion = schemas.BoolSchema
                    lastBookingDate = schemas.DateSchema
                    notes = schemas.StrSchema
                    orderNumber = schemas.StrSchema
                    organizationLabel = schemas.StrSchema
                    paymentTerm = schemas.StrSchema
                    
                    
                    class ratePlans(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['GETSubscriptionRatePlanType']:
                                return GETSubscriptionRatePlanType
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['GETSubscriptionRatePlanType'], typing.List['GETSubscriptionRatePlanType']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'ratePlans':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'GETSubscriptionRatePlanType':
                            return super().__getitem__(i)
                    renewalSetting = schemas.StrSchema
                    renewalTerm = schemas.Int64Schema
                    renewalTermPeriodType = schemas.StrSchema
                    revision = schemas.StrSchema
                    sequenceSetId = schemas.StrSchema
                    sequenceSetName = schemas.StrSchema
                    serviceActivationDate = schemas.DateSchema
                
                    @staticmethod
                    def soldToContact() -> typing.Type['GETAccountSummaryTypeSoldToContact']:
                        return GETAccountSummaryTypeSoldToContact
                    status = schemas.StrSchema
                    
                    
                    class statusHistory(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['GETSubscriptionStatusHistoryType']:
                                return GETSubscriptionStatusHistoryType
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['GETSubscriptionStatusHistoryType'], typing.List['GETSubscriptionStatusHistoryType']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'statusHistory':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'GETSubscriptionStatusHistoryType':
                            return super().__getitem__(i)
                    subscriptionEndDate = schemas.DateSchema
                    subscriptionNumber = schemas.StrSchema
                    subscriptionStartDate = schemas.DateSchema
                    success = schemas.BoolSchema
                    termEndDate = schemas.DateSchema
                    termStartDate = schemas.DateSchema
                    termType = schemas.StrSchema
                    totalContractedValue = schemas.NumberSchema
                    __annotations__ = {
                        "version": version,
                        "accountId": accountId,
                        "accountName": accountName,
                        "accountNumber": accountNumber,
                        "autoRenew": autoRenew,
                        "billToContact": billToContact,
                        "cancelReason": cancelReason,
                        "contractEffectiveDate": contractEffectiveDate,
                        "contractedMrr": contractedMrr,
                        "currency": currency,
                        "currentTerm": currentTerm,
                        "currentTermPeriodType": currentTermPeriodType,
                        "customerAcceptanceDate": customerAcceptanceDate,
                        "externallyManagedBy": externallyManagedBy,
                        "id": id,
                        "initialTerm": initialTerm,
                        "initialTermPeriodType": initialTermPeriodType,
                        "invoiceGroupNumber": invoiceGroupNumber,
                        "invoiceOwnerAccountId": invoiceOwnerAccountId,
                        "invoiceOwnerAccountName": invoiceOwnerAccountName,
                        "invoiceOwnerAccountNumber": invoiceOwnerAccountNumber,
                        "invoiceScheduleId": invoiceScheduleId,
                        "invoiceSeparately": invoiceSeparately,
                        "invoiceTemplateId": invoiceTemplateId,
                        "invoiceTemplateName": invoiceTemplateName,
                        "isLatestVersion": isLatestVersion,
                        "lastBookingDate": lastBookingDate,
                        "notes": notes,
                        "orderNumber": orderNumber,
                        "organizationLabel": organizationLabel,
                        "paymentTerm": paymentTerm,
                        "ratePlans": ratePlans,
                        "renewalSetting": renewalSetting,
                        "renewalTerm": renewalTerm,
                        "renewalTermPeriodType": renewalTermPeriodType,
                        "revision": revision,
                        "sequenceSetId": sequenceSetId,
                        "sequenceSetName": sequenceSetName,
                        "serviceActivationDate": serviceActivationDate,
                        "soldToContact": soldToContact,
                        "status": status,
                        "statusHistory": statusHistory,
                        "subscriptionEndDate": subscriptionEndDate,
                        "subscriptionNumber": subscriptionNumber,
                        "subscriptionStartDate": subscriptionStartDate,
                        "success": success,
                        "termEndDate": termEndDate,
                        "termStartDate": termStartDate,
                        "termType": termType,
                        "totalContractedValue": totalContractedValue,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["accountName"]) -> MetaOapg.properties.accountName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["accountNumber"]) -> MetaOapg.properties.accountNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["autoRenew"]) -> MetaOapg.properties.autoRenew: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["billToContact"]) -> 'GETAccountSummaryTypeBillToContact': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cancelReason"]) -> MetaOapg.properties.cancelReason: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contractEffectiveDate"]) -> MetaOapg.properties.contractEffectiveDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contractedMrr"]) -> MetaOapg.properties.contractedMrr: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["currentTerm"]) -> MetaOapg.properties.currentTerm: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["currentTermPeriodType"]) -> MetaOapg.properties.currentTermPeriodType: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["customerAcceptanceDate"]) -> MetaOapg.properties.customerAcceptanceDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["externallyManagedBy"]) -> MetaOapg.properties.externallyManagedBy: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["initialTerm"]) -> MetaOapg.properties.initialTerm: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["initialTermPeriodType"]) -> MetaOapg.properties.initialTermPeriodType: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceGroupNumber"]) -> MetaOapg.properties.invoiceGroupNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceOwnerAccountId"]) -> MetaOapg.properties.invoiceOwnerAccountId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceOwnerAccountName"]) -> MetaOapg.properties.invoiceOwnerAccountName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceOwnerAccountNumber"]) -> MetaOapg.properties.invoiceOwnerAccountNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceScheduleId"]) -> MetaOapg.properties.invoiceScheduleId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceSeparately"]) -> MetaOapg.properties.invoiceSeparately: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceTemplateId"]) -> MetaOapg.properties.invoiceTemplateId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceTemplateName"]) -> MetaOapg.properties.invoiceTemplateName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["isLatestVersion"]) -> MetaOapg.properties.isLatestVersion: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["lastBookingDate"]) -> MetaOapg.properties.lastBookingDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["orderNumber"]) -> MetaOapg.properties.orderNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["organizationLabel"]) -> MetaOapg.properties.organizationLabel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["paymentTerm"]) -> MetaOapg.properties.paymentTerm: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["ratePlans"]) -> MetaOapg.properties.ratePlans: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["renewalSetting"]) -> MetaOapg.properties.renewalSetting: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["renewalTerm"]) -> MetaOapg.properties.renewalTerm: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["renewalTermPeriodType"]) -> MetaOapg.properties.renewalTermPeriodType: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["revision"]) -> MetaOapg.properties.revision: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sequenceSetId"]) -> MetaOapg.properties.sequenceSetId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sequenceSetName"]) -> MetaOapg.properties.sequenceSetName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["serviceActivationDate"]) -> MetaOapg.properties.serviceActivationDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["soldToContact"]) -> 'GETAccountSummaryTypeSoldToContact': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["statusHistory"]) -> MetaOapg.properties.statusHistory: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["subscriptionEndDate"]) -> MetaOapg.properties.subscriptionEndDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["subscriptionNumber"]) -> MetaOapg.properties.subscriptionNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["subscriptionStartDate"]) -> MetaOapg.properties.subscriptionStartDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["termEndDate"]) -> MetaOapg.properties.termEndDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["termStartDate"]) -> MetaOapg.properties.termStartDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["termType"]) -> MetaOapg.properties.termType: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["totalContractedValue"]) -> MetaOapg.properties.totalContractedValue: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "accountId", "accountName", "accountNumber", "autoRenew", "billToContact", "cancelReason", "contractEffectiveDate", "contractedMrr", "currency", "currentTerm", "currentTermPeriodType", "customerAcceptanceDate", "externallyManagedBy", "id", "initialTerm", "initialTermPeriodType", "invoiceGroupNumber", "invoiceOwnerAccountId", "invoiceOwnerAccountName", "invoiceOwnerAccountNumber", "invoiceScheduleId", "invoiceSeparately", "invoiceTemplateId", "invoiceTemplateName", "isLatestVersion", "lastBookingDate", "notes", "orderNumber", "organizationLabel", "paymentTerm", "ratePlans", "renewalSetting", "renewalTerm", "renewalTermPeriodType", "revision", "sequenceSetId", "sequenceSetName", "serviceActivationDate", "soldToContact", "status", "statusHistory", "subscriptionEndDate", "subscriptionNumber", "subscriptionStartDate", "success", "termEndDate", "termStartDate", "termType", "totalContractedValue", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> typing.Union[MetaOapg.properties.accountId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["accountName"]) -> typing.Union[MetaOapg.properties.accountName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["accountNumber"]) -> typing.Union[MetaOapg.properties.accountNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["autoRenew"]) -> typing.Union[MetaOapg.properties.autoRenew, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["billToContact"]) -> typing.Union['GETAccountSummaryTypeBillToContact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cancelReason"]) -> typing.Union[MetaOapg.properties.cancelReason, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contractEffectiveDate"]) -> typing.Union[MetaOapg.properties.contractEffectiveDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contractedMrr"]) -> typing.Union[MetaOapg.properties.contractedMrr, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["currentTerm"]) -> typing.Union[MetaOapg.properties.currentTerm, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["currentTermPeriodType"]) -> typing.Union[MetaOapg.properties.currentTermPeriodType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["customerAcceptanceDate"]) -> typing.Union[MetaOapg.properties.customerAcceptanceDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["externallyManagedBy"]) -> typing.Union[MetaOapg.properties.externallyManagedBy, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["initialTerm"]) -> typing.Union[MetaOapg.properties.initialTerm, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["initialTermPeriodType"]) -> typing.Union[MetaOapg.properties.initialTermPeriodType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceGroupNumber"]) -> typing.Union[MetaOapg.properties.invoiceGroupNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceOwnerAccountId"]) -> typing.Union[MetaOapg.properties.invoiceOwnerAccountId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceOwnerAccountName"]) -> typing.Union[MetaOapg.properties.invoiceOwnerAccountName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceOwnerAccountNumber"]) -> typing.Union[MetaOapg.properties.invoiceOwnerAccountNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceScheduleId"]) -> typing.Union[MetaOapg.properties.invoiceScheduleId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceSeparately"]) -> typing.Union[MetaOapg.properties.invoiceSeparately, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceTemplateId"]) -> typing.Union[MetaOapg.properties.invoiceTemplateId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceTemplateName"]) -> typing.Union[MetaOapg.properties.invoiceTemplateName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["isLatestVersion"]) -> typing.Union[MetaOapg.properties.isLatestVersion, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["lastBookingDate"]) -> typing.Union[MetaOapg.properties.lastBookingDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["orderNumber"]) -> typing.Union[MetaOapg.properties.orderNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["organizationLabel"]) -> typing.Union[MetaOapg.properties.organizationLabel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["paymentTerm"]) -> typing.Union[MetaOapg.properties.paymentTerm, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["ratePlans"]) -> typing.Union[MetaOapg.properties.ratePlans, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["renewalSetting"]) -> typing.Union[MetaOapg.properties.renewalSetting, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["renewalTerm"]) -> typing.Union[MetaOapg.properties.renewalTerm, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["renewalTermPeriodType"]) -> typing.Union[MetaOapg.properties.renewalTermPeriodType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["revision"]) -> typing.Union[MetaOapg.properties.revision, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sequenceSetId"]) -> typing.Union[MetaOapg.properties.sequenceSetId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sequenceSetName"]) -> typing.Union[MetaOapg.properties.sequenceSetName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["serviceActivationDate"]) -> typing.Union[MetaOapg.properties.serviceActivationDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["soldToContact"]) -> typing.Union['GETAccountSummaryTypeSoldToContact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["statusHistory"]) -> typing.Union[MetaOapg.properties.statusHistory, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["subscriptionEndDate"]) -> typing.Union[MetaOapg.properties.subscriptionEndDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["subscriptionNumber"]) -> typing.Union[MetaOapg.properties.subscriptionNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["subscriptionStartDate"]) -> typing.Union[MetaOapg.properties.subscriptionStartDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> typing.Union[MetaOapg.properties.success, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["termEndDate"]) -> typing.Union[MetaOapg.properties.termEndDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["termStartDate"]) -> typing.Union[MetaOapg.properties.termStartDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["termType"]) -> typing.Union[MetaOapg.properties.termType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["totalContractedValue"]) -> typing.Union[MetaOapg.properties.totalContractedValue, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "accountId", "accountName", "accountNumber", "autoRenew", "billToContact", "cancelReason", "contractEffectiveDate", "contractedMrr", "currency", "currentTerm", "currentTermPeriodType", "customerAcceptanceDate", "externallyManagedBy", "id", "initialTerm", "initialTermPeriodType", "invoiceGroupNumber", "invoiceOwnerAccountId", "invoiceOwnerAccountName", "invoiceOwnerAccountNumber", "invoiceScheduleId", "invoiceSeparately", "invoiceTemplateId", "invoiceTemplateName", "isLatestVersion", "lastBookingDate", "notes", "orderNumber", "organizationLabel", "paymentTerm", "ratePlans", "renewalSetting", "renewalTerm", "renewalTermPeriodType", "revision", "sequenceSetId", "sequenceSetName", "serviceActivationDate", "soldToContact", "status", "statusHistory", "subscriptionEndDate", "subscriptionNumber", "subscriptionStartDate", "success", "termEndDate", "termStartDate", "termType", "totalContractedValue", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                version: typing.Union[MetaOapg.properties.version, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                accountId: typing.Union[MetaOapg.properties.accountId, str, schemas.Unset] = schemas.unset,
                accountName: typing.Union[MetaOapg.properties.accountName, str, schemas.Unset] = schemas.unset,
                accountNumber: typing.Union[MetaOapg.properties.accountNumber, str, schemas.Unset] = schemas.unset,
                autoRenew: typing.Union[MetaOapg.properties.autoRenew, bool, schemas.Unset] = schemas.unset,
                billToContact: typing.Union['GETAccountSummaryTypeBillToContact', schemas.Unset] = schemas.unset,
                cancelReason: typing.Union[MetaOapg.properties.cancelReason, str, schemas.Unset] = schemas.unset,
                contractEffectiveDate: typing.Union[MetaOapg.properties.contractEffectiveDate, str, date, schemas.Unset] = schemas.unset,
                contractedMrr: typing.Union[MetaOapg.properties.contractedMrr, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
                currentTerm: typing.Union[MetaOapg.properties.currentTerm, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                currentTermPeriodType: typing.Union[MetaOapg.properties.currentTermPeriodType, str, schemas.Unset] = schemas.unset,
                customerAcceptanceDate: typing.Union[MetaOapg.properties.customerAcceptanceDate, str, date, schemas.Unset] = schemas.unset,
                externallyManagedBy: typing.Union[MetaOapg.properties.externallyManagedBy, str, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                initialTerm: typing.Union[MetaOapg.properties.initialTerm, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                initialTermPeriodType: typing.Union[MetaOapg.properties.initialTermPeriodType, str, schemas.Unset] = schemas.unset,
                invoiceGroupNumber: typing.Union[MetaOapg.properties.invoiceGroupNumber, None, str, schemas.Unset] = schemas.unset,
                invoiceOwnerAccountId: typing.Union[MetaOapg.properties.invoiceOwnerAccountId, str, schemas.Unset] = schemas.unset,
                invoiceOwnerAccountName: typing.Union[MetaOapg.properties.invoiceOwnerAccountName, str, schemas.Unset] = schemas.unset,
                invoiceOwnerAccountNumber: typing.Union[MetaOapg.properties.invoiceOwnerAccountNumber, str, schemas.Unset] = schemas.unset,
                invoiceScheduleId: typing.Union[MetaOapg.properties.invoiceScheduleId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                invoiceSeparately: typing.Union[MetaOapg.properties.invoiceSeparately, str, schemas.Unset] = schemas.unset,
                invoiceTemplateId: typing.Union[MetaOapg.properties.invoiceTemplateId, str, schemas.Unset] = schemas.unset,
                invoiceTemplateName: typing.Union[MetaOapg.properties.invoiceTemplateName, str, schemas.Unset] = schemas.unset,
                isLatestVersion: typing.Union[MetaOapg.properties.isLatestVersion, bool, schemas.Unset] = schemas.unset,
                lastBookingDate: typing.Union[MetaOapg.properties.lastBookingDate, str, date, schemas.Unset] = schemas.unset,
                notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
                orderNumber: typing.Union[MetaOapg.properties.orderNumber, str, schemas.Unset] = schemas.unset,
                organizationLabel: typing.Union[MetaOapg.properties.organizationLabel, str, schemas.Unset] = schemas.unset,
                paymentTerm: typing.Union[MetaOapg.properties.paymentTerm, str, schemas.Unset] = schemas.unset,
                ratePlans: typing.Union[MetaOapg.properties.ratePlans, list, tuple, schemas.Unset] = schemas.unset,
                renewalSetting: typing.Union[MetaOapg.properties.renewalSetting, str, schemas.Unset] = schemas.unset,
                renewalTerm: typing.Union[MetaOapg.properties.renewalTerm, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                renewalTermPeriodType: typing.Union[MetaOapg.properties.renewalTermPeriodType, str, schemas.Unset] = schemas.unset,
                revision: typing.Union[MetaOapg.properties.revision, str, schemas.Unset] = schemas.unset,
                sequenceSetId: typing.Union[MetaOapg.properties.sequenceSetId, str, schemas.Unset] = schemas.unset,
                sequenceSetName: typing.Union[MetaOapg.properties.sequenceSetName, str, schemas.Unset] = schemas.unset,
                serviceActivationDate: typing.Union[MetaOapg.properties.serviceActivationDate, str, date, schemas.Unset] = schemas.unset,
                soldToContact: typing.Union['GETAccountSummaryTypeSoldToContact', schemas.Unset] = schemas.unset,
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                statusHistory: typing.Union[MetaOapg.properties.statusHistory, list, tuple, schemas.Unset] = schemas.unset,
                subscriptionEndDate: typing.Union[MetaOapg.properties.subscriptionEndDate, str, date, schemas.Unset] = schemas.unset,
                subscriptionNumber: typing.Union[MetaOapg.properties.subscriptionNumber, str, schemas.Unset] = schemas.unset,
                subscriptionStartDate: typing.Union[MetaOapg.properties.subscriptionStartDate, str, date, schemas.Unset] = schemas.unset,
                success: typing.Union[MetaOapg.properties.success, bool, schemas.Unset] = schemas.unset,
                termEndDate: typing.Union[MetaOapg.properties.termEndDate, str, date, schemas.Unset] = schemas.unset,
                termStartDate: typing.Union[MetaOapg.properties.termStartDate, str, date, schemas.Unset] = schemas.unset,
                termType: typing.Union[MetaOapg.properties.termType, str, schemas.Unset] = schemas.unset,
                totalContractedValue: typing.Union[MetaOapg.properties.totalContractedValue, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    version=version,
                    accountId=accountId,
                    accountName=accountName,
                    accountNumber=accountNumber,
                    autoRenew=autoRenew,
                    billToContact=billToContact,
                    cancelReason=cancelReason,
                    contractEffectiveDate=contractEffectiveDate,
                    contractedMrr=contractedMrr,
                    currency=currency,
                    currentTerm=currentTerm,
                    currentTermPeriodType=currentTermPeriodType,
                    customerAcceptanceDate=customerAcceptanceDate,
                    externallyManagedBy=externallyManagedBy,
                    id=id,
                    initialTerm=initialTerm,
                    initialTermPeriodType=initialTermPeriodType,
                    invoiceGroupNumber=invoiceGroupNumber,
                    invoiceOwnerAccountId=invoiceOwnerAccountId,
                    invoiceOwnerAccountName=invoiceOwnerAccountName,
                    invoiceOwnerAccountNumber=invoiceOwnerAccountNumber,
                    invoiceScheduleId=invoiceScheduleId,
                    invoiceSeparately=invoiceSeparately,
                    invoiceTemplateId=invoiceTemplateId,
                    invoiceTemplateName=invoiceTemplateName,
                    isLatestVersion=isLatestVersion,
                    lastBookingDate=lastBookingDate,
                    notes=notes,
                    orderNumber=orderNumber,
                    organizationLabel=organizationLabel,
                    paymentTerm=paymentTerm,
                    ratePlans=ratePlans,
                    renewalSetting=renewalSetting,
                    renewalTerm=renewalTerm,
                    renewalTermPeriodType=renewalTermPeriodType,
                    revision=revision,
                    sequenceSetId=sequenceSetId,
                    sequenceSetName=sequenceSetName,
                    serviceActivationDate=serviceActivationDate,
                    soldToContact=soldToContact,
                    status=status,
                    statusHistory=statusHistory,
                    subscriptionEndDate=subscriptionEndDate,
                    subscriptionNumber=subscriptionNumber,
                    subscriptionStartDate=subscriptionStartDate,
                    success=success,
                    termEndDate=termEndDate,
                    termStartDate=termStartDate,
                    termType=termType,
                    totalContractedValue=totalContractedValue,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.all_of_0,
                SubscriptionObjectQTFields,
                SubscriptionObjectNSFields,
                SubscriptionObjectCustomFields,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GETSubscriptionTypeWithSuccess':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from zuora_python_sdk.model.get_account_summary_type_bill_to_contact import GETAccountSummaryTypeBillToContact
from zuora_python_sdk.model.get_account_summary_type_sold_to_contact import GETAccountSummaryTypeSoldToContact
from zuora_python_sdk.model.get_subscription_rate_plan_type import GETSubscriptionRatePlanType
from zuora_python_sdk.model.get_subscription_status_history_type import GETSubscriptionStatusHistoryType
from zuora_python_sdk.model.subscription_object_custom_fields import SubscriptionObjectCustomFields
from zuora_python_sdk.model.subscription_object_ns_fields import SubscriptionObjectNSFields
from zuora_python_sdk.model.subscription_object_qt_fields import SubscriptionObjectQTFields

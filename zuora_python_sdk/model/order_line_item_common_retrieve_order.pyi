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


class OrderLineItemCommonRetrieveOrder(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            UOM = schemas.StrSchema
            accountingCode = schemas.StrSchema
            adjustmentLiabilityAccountingCode = schemas.StrSchema
            adjustmentRevenueAccountingCode = schemas.StrSchema
            amountPerUnit = schemas.NumberSchema
            billTargetDate = schemas.DateSchema
            billTo = schemas.StrSchema
            billToSnapshotId = schemas.StrSchema
            
            
            class billingRule(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRIGGER_WITHOUT_FULFILLMENT(cls):
                    return cls("TriggerWithoutFulfillment")
                
                @schemas.classproperty
                def TRIGGER_AS_FULFILLMENT_OCCURS(cls):
                    return cls("TriggerAsFulfillmentOccurs")
            contractAssetAccountingCode = schemas.StrSchema
            contractLiabilityAccountingCode = schemas.StrSchema
            contractRecognizedRevenueAccountingCode = schemas.StrSchema
            currency = schemas.StrSchema
        
            @staticmethod
            def customFields() -> typing.Type['OrderLineItemCustomFields']:
                return OrderLineItemCustomFields
            deferredRevenueAccountingCode = schemas.StrSchema
            discount = schemas.NumberSchema
            excludeItemBillingFromRevenueAccounting = schemas.BoolSchema
            excludeItemBookingFromRevenueAccounting = schemas.BoolSchema
            inlineDiscountPerUnit = schemas.NumberSchema
            
            
            class inlineDiscountType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PERCENTAGE(cls):
                    return cls("Percentage")
                
                @schemas.classproperty
                def FIXED_AMOUNT(cls):
                    return cls("FixedAmount")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("None")
            invoiceOwnerAccountId = schemas.StrSchema
            invoiceOwnerAccountName = schemas.StrSchema
            invoiceOwnerAccountNumber = schemas.StrSchema
            isAllocationEligible = schemas.BoolSchema
            isUnbilled = schemas.BoolSchema
            
            
            class itemCategory(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SALES(cls):
                    return cls("Sales")
                
                @schemas.classproperty
                def RETURN(cls):
                    return cls("Return")
            itemName = schemas.StrSchema
            
            
            class itemState(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EXECUTING(cls):
                    return cls("Executing")
                
                @schemas.classproperty
                def BOOKED(cls):
                    return cls("Booked")
                
                @schemas.classproperty
                def SENT_TO_BILLING(cls):
                    return cls("SentToBilling")
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("Complete")
                
                @schemas.classproperty
                def CANCELLED(cls):
                    return cls("Cancelled")
            
            
            class itemType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PRODUCT(cls):
                    return cls("Product")
                
                @schemas.classproperty
                def FEE(cls):
                    return cls("Fee")
                
                @schemas.classproperty
                def SERVICES(cls):
                    return cls("Services")
            listPrice = schemas.NumberSchema
            listPricePerUnit = schemas.NumberSchema
            originalOrderId = schemas.StrSchema
            originalOrderLineItemId = schemas.StrSchema
            originalOrderLineItemNumber = schemas.StrSchema
            originalOrderNumber = schemas.StrSchema
            ownerAccountId = schemas.StrSchema
            ownerAccountName = schemas.StrSchema
            ownerAccountNumber = schemas.StrSchema
            productCode = schemas.StrSchema
            productRatePlanChargeId = schemas.StrSchema
            purchaseOrderNumber = schemas.StrSchema
            quantity = schemas.NumberSchema
            quantityAvailableForReturn = schemas.NumberSchema
            quantityFulfilled = schemas.NumberSchema
            quantityPendingFulfillment = schemas.NumberSchema
            recognizedRevenueAccountingCode = schemas.StrSchema
            relatedSubscriptionNumber = schemas.StrSchema
            requiresFulfillment = schemas.BoolSchema
            revenueRecognitionRule = schemas.StrSchema
            
            
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
            sequenceSetId = schemas.StrSchema
            soldTo = schemas.StrSchema
            soldToSnapshotId = schemas.StrSchema
            taxCode = schemas.StrSchema
            
            
            class taxMode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TAX_INCLUSIVE(cls):
                    return cls("TaxInclusive")
                
                @schemas.classproperty
                def TAX_EXCLUSIVE(cls):
                    return cls("TaxExclusive")
            transactionEndDate = schemas.DateSchema
            transactionStartDate = schemas.DateSchema
            unbilledReceivablesAccountingCode = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "UOM": UOM,
                "accountingCode": accountingCode,
                "adjustmentLiabilityAccountingCode": adjustmentLiabilityAccountingCode,
                "adjustmentRevenueAccountingCode": adjustmentRevenueAccountingCode,
                "amountPerUnit": amountPerUnit,
                "billTargetDate": billTargetDate,
                "billTo": billTo,
                "billToSnapshotId": billToSnapshotId,
                "billingRule": billingRule,
                "contractAssetAccountingCode": contractAssetAccountingCode,
                "contractLiabilityAccountingCode": contractLiabilityAccountingCode,
                "contractRecognizedRevenueAccountingCode": contractRecognizedRevenueAccountingCode,
                "currency": currency,
                "customFields": customFields,
                "deferredRevenueAccountingCode": deferredRevenueAccountingCode,
                "discount": discount,
                "excludeItemBillingFromRevenueAccounting": excludeItemBillingFromRevenueAccounting,
                "excludeItemBookingFromRevenueAccounting": excludeItemBookingFromRevenueAccounting,
                "inlineDiscountPerUnit": inlineDiscountPerUnit,
                "inlineDiscountType": inlineDiscountType,
                "invoiceOwnerAccountId": invoiceOwnerAccountId,
                "invoiceOwnerAccountName": invoiceOwnerAccountName,
                "invoiceOwnerAccountNumber": invoiceOwnerAccountNumber,
                "isAllocationEligible": isAllocationEligible,
                "isUnbilled": isUnbilled,
                "itemCategory": itemCategory,
                "itemName": itemName,
                "itemState": itemState,
                "itemType": itemType,
                "listPrice": listPrice,
                "listPricePerUnit": listPricePerUnit,
                "originalOrderId": originalOrderId,
                "originalOrderLineItemId": originalOrderLineItemId,
                "originalOrderLineItemNumber": originalOrderLineItemNumber,
                "originalOrderNumber": originalOrderNumber,
                "ownerAccountId": ownerAccountId,
                "ownerAccountName": ownerAccountName,
                "ownerAccountNumber": ownerAccountNumber,
                "productCode": productCode,
                "productRatePlanChargeId": productRatePlanChargeId,
                "purchaseOrderNumber": purchaseOrderNumber,
                "quantity": quantity,
                "quantityAvailableForReturn": quantityAvailableForReturn,
                "quantityFulfilled": quantityFulfilled,
                "quantityPendingFulfillment": quantityPendingFulfillment,
                "recognizedRevenueAccountingCode": recognizedRevenueAccountingCode,
                "relatedSubscriptionNumber": relatedSubscriptionNumber,
                "requiresFulfillment": requiresFulfillment,
                "revenueRecognitionRule": revenueRecognitionRule,
                "revenueRecognitionTiming": revenueRecognitionTiming,
                "revenueAmortizationMethod": revenueAmortizationMethod,
                "sequenceSetId": sequenceSetId,
                "soldTo": soldTo,
                "soldToSnapshotId": soldToSnapshotId,
                "taxCode": taxCode,
                "taxMode": taxMode,
                "transactionEndDate": transactionEndDate,
                "transactionStartDate": transactionStartDate,
                "unbilledReceivablesAccountingCode": unbilledReceivablesAccountingCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UOM"]) -> MetaOapg.properties.UOM: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountingCode"]) -> MetaOapg.properties.accountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adjustmentLiabilityAccountingCode"]) -> MetaOapg.properties.adjustmentLiabilityAccountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adjustmentRevenueAccountingCode"]) -> MetaOapg.properties.adjustmentRevenueAccountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amountPerUnit"]) -> MetaOapg.properties.amountPerUnit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billTargetDate"]) -> MetaOapg.properties.billTargetDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billTo"]) -> MetaOapg.properties.billTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billToSnapshotId"]) -> MetaOapg.properties.billToSnapshotId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingRule"]) -> MetaOapg.properties.billingRule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractAssetAccountingCode"]) -> MetaOapg.properties.contractAssetAccountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractLiabilityAccountingCode"]) -> MetaOapg.properties.contractLiabilityAccountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractRecognizedRevenueAccountingCode"]) -> MetaOapg.properties.contractRecognizedRevenueAccountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> 'OrderLineItemCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deferredRevenueAccountingCode"]) -> MetaOapg.properties.deferredRevenueAccountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discount"]) -> MetaOapg.properties.discount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excludeItemBillingFromRevenueAccounting"]) -> MetaOapg.properties.excludeItemBillingFromRevenueAccounting: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excludeItemBookingFromRevenueAccounting"]) -> MetaOapg.properties.excludeItemBookingFromRevenueAccounting: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inlineDiscountPerUnit"]) -> MetaOapg.properties.inlineDiscountPerUnit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inlineDiscountType"]) -> MetaOapg.properties.inlineDiscountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoiceOwnerAccountId"]) -> MetaOapg.properties.invoiceOwnerAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoiceOwnerAccountName"]) -> MetaOapg.properties.invoiceOwnerAccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoiceOwnerAccountNumber"]) -> MetaOapg.properties.invoiceOwnerAccountNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAllocationEligible"]) -> MetaOapg.properties.isAllocationEligible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isUnbilled"]) -> MetaOapg.properties.isUnbilled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemCategory"]) -> MetaOapg.properties.itemCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemName"]) -> MetaOapg.properties.itemName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemState"]) -> MetaOapg.properties.itemState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemType"]) -> MetaOapg.properties.itemType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["listPrice"]) -> MetaOapg.properties.listPrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["listPricePerUnit"]) -> MetaOapg.properties.listPricePerUnit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originalOrderId"]) -> MetaOapg.properties.originalOrderId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originalOrderLineItemId"]) -> MetaOapg.properties.originalOrderLineItemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originalOrderLineItemNumber"]) -> MetaOapg.properties.originalOrderLineItemNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originalOrderNumber"]) -> MetaOapg.properties.originalOrderNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerAccountId"]) -> MetaOapg.properties.ownerAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerAccountName"]) -> MetaOapg.properties.ownerAccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerAccountNumber"]) -> MetaOapg.properties.ownerAccountNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productCode"]) -> MetaOapg.properties.productCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productRatePlanChargeId"]) -> MetaOapg.properties.productRatePlanChargeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchaseOrderNumber"]) -> MetaOapg.properties.purchaseOrderNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantityAvailableForReturn"]) -> MetaOapg.properties.quantityAvailableForReturn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantityFulfilled"]) -> MetaOapg.properties.quantityFulfilled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantityPendingFulfillment"]) -> MetaOapg.properties.quantityPendingFulfillment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recognizedRevenueAccountingCode"]) -> MetaOapg.properties.recognizedRevenueAccountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relatedSubscriptionNumber"]) -> MetaOapg.properties.relatedSubscriptionNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requiresFulfillment"]) -> MetaOapg.properties.requiresFulfillment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenueRecognitionRule"]) -> MetaOapg.properties.revenueRecognitionRule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenueRecognitionTiming"]) -> MetaOapg.properties.revenueRecognitionTiming: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenueAmortizationMethod"]) -> MetaOapg.properties.revenueAmortizationMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequenceSetId"]) -> MetaOapg.properties.sequenceSetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["soldTo"]) -> MetaOapg.properties.soldTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["soldToSnapshotId"]) -> MetaOapg.properties.soldToSnapshotId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCode"]) -> MetaOapg.properties.taxCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxMode"]) -> MetaOapg.properties.taxMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionEndDate"]) -> MetaOapg.properties.transactionEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionStartDate"]) -> MetaOapg.properties.transactionStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unbilledReceivablesAccountingCode"]) -> MetaOapg.properties.unbilledReceivablesAccountingCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "UOM", "accountingCode", "adjustmentLiabilityAccountingCode", "adjustmentRevenueAccountingCode", "amountPerUnit", "billTargetDate", "billTo", "billToSnapshotId", "billingRule", "contractAssetAccountingCode", "contractLiabilityAccountingCode", "contractRecognizedRevenueAccountingCode", "currency", "customFields", "deferredRevenueAccountingCode", "discount", "excludeItemBillingFromRevenueAccounting", "excludeItemBookingFromRevenueAccounting", "inlineDiscountPerUnit", "inlineDiscountType", "invoiceOwnerAccountId", "invoiceOwnerAccountName", "invoiceOwnerAccountNumber", "isAllocationEligible", "isUnbilled", "itemCategory", "itemName", "itemState", "itemType", "listPrice", "listPricePerUnit", "originalOrderId", "originalOrderLineItemId", "originalOrderLineItemNumber", "originalOrderNumber", "ownerAccountId", "ownerAccountName", "ownerAccountNumber", "productCode", "productRatePlanChargeId", "purchaseOrderNumber", "quantity", "quantityAvailableForReturn", "quantityFulfilled", "quantityPendingFulfillment", "recognizedRevenueAccountingCode", "relatedSubscriptionNumber", "requiresFulfillment", "revenueRecognitionRule", "revenueRecognitionTiming", "revenueAmortizationMethod", "sequenceSetId", "soldTo", "soldToSnapshotId", "taxCode", "taxMode", "transactionEndDate", "transactionStartDate", "unbilledReceivablesAccountingCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UOM"]) -> typing.Union[MetaOapg.properties.UOM, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountingCode"]) -> typing.Union[MetaOapg.properties.accountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adjustmentLiabilityAccountingCode"]) -> typing.Union[MetaOapg.properties.adjustmentLiabilityAccountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adjustmentRevenueAccountingCode"]) -> typing.Union[MetaOapg.properties.adjustmentRevenueAccountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amountPerUnit"]) -> typing.Union[MetaOapg.properties.amountPerUnit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billTargetDate"]) -> typing.Union[MetaOapg.properties.billTargetDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billTo"]) -> typing.Union[MetaOapg.properties.billTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billToSnapshotId"]) -> typing.Union[MetaOapg.properties.billToSnapshotId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingRule"]) -> typing.Union[MetaOapg.properties.billingRule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractAssetAccountingCode"]) -> typing.Union[MetaOapg.properties.contractAssetAccountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractLiabilityAccountingCode"]) -> typing.Union[MetaOapg.properties.contractLiabilityAccountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractRecognizedRevenueAccountingCode"]) -> typing.Union[MetaOapg.properties.contractRecognizedRevenueAccountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union['OrderLineItemCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deferredRevenueAccountingCode"]) -> typing.Union[MetaOapg.properties.deferredRevenueAccountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discount"]) -> typing.Union[MetaOapg.properties.discount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excludeItemBillingFromRevenueAccounting"]) -> typing.Union[MetaOapg.properties.excludeItemBillingFromRevenueAccounting, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excludeItemBookingFromRevenueAccounting"]) -> typing.Union[MetaOapg.properties.excludeItemBookingFromRevenueAccounting, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inlineDiscountPerUnit"]) -> typing.Union[MetaOapg.properties.inlineDiscountPerUnit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inlineDiscountType"]) -> typing.Union[MetaOapg.properties.inlineDiscountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoiceOwnerAccountId"]) -> typing.Union[MetaOapg.properties.invoiceOwnerAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoiceOwnerAccountName"]) -> typing.Union[MetaOapg.properties.invoiceOwnerAccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoiceOwnerAccountNumber"]) -> typing.Union[MetaOapg.properties.invoiceOwnerAccountNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAllocationEligible"]) -> typing.Union[MetaOapg.properties.isAllocationEligible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isUnbilled"]) -> typing.Union[MetaOapg.properties.isUnbilled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemCategory"]) -> typing.Union[MetaOapg.properties.itemCategory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemName"]) -> typing.Union[MetaOapg.properties.itemName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemState"]) -> typing.Union[MetaOapg.properties.itemState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemType"]) -> typing.Union[MetaOapg.properties.itemType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["listPrice"]) -> typing.Union[MetaOapg.properties.listPrice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["listPricePerUnit"]) -> typing.Union[MetaOapg.properties.listPricePerUnit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originalOrderId"]) -> typing.Union[MetaOapg.properties.originalOrderId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originalOrderLineItemId"]) -> typing.Union[MetaOapg.properties.originalOrderLineItemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originalOrderLineItemNumber"]) -> typing.Union[MetaOapg.properties.originalOrderLineItemNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originalOrderNumber"]) -> typing.Union[MetaOapg.properties.originalOrderNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerAccountId"]) -> typing.Union[MetaOapg.properties.ownerAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerAccountName"]) -> typing.Union[MetaOapg.properties.ownerAccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerAccountNumber"]) -> typing.Union[MetaOapg.properties.ownerAccountNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productCode"]) -> typing.Union[MetaOapg.properties.productCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productRatePlanChargeId"]) -> typing.Union[MetaOapg.properties.productRatePlanChargeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchaseOrderNumber"]) -> typing.Union[MetaOapg.properties.purchaseOrderNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> typing.Union[MetaOapg.properties.quantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantityAvailableForReturn"]) -> typing.Union[MetaOapg.properties.quantityAvailableForReturn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantityFulfilled"]) -> typing.Union[MetaOapg.properties.quantityFulfilled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantityPendingFulfillment"]) -> typing.Union[MetaOapg.properties.quantityPendingFulfillment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recognizedRevenueAccountingCode"]) -> typing.Union[MetaOapg.properties.recognizedRevenueAccountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relatedSubscriptionNumber"]) -> typing.Union[MetaOapg.properties.relatedSubscriptionNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requiresFulfillment"]) -> typing.Union[MetaOapg.properties.requiresFulfillment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenueRecognitionRule"]) -> typing.Union[MetaOapg.properties.revenueRecognitionRule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenueRecognitionTiming"]) -> typing.Union[MetaOapg.properties.revenueRecognitionTiming, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenueAmortizationMethod"]) -> typing.Union[MetaOapg.properties.revenueAmortizationMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequenceSetId"]) -> typing.Union[MetaOapg.properties.sequenceSetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["soldTo"]) -> typing.Union[MetaOapg.properties.soldTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["soldToSnapshotId"]) -> typing.Union[MetaOapg.properties.soldToSnapshotId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCode"]) -> typing.Union[MetaOapg.properties.taxCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxMode"]) -> typing.Union[MetaOapg.properties.taxMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionEndDate"]) -> typing.Union[MetaOapg.properties.transactionEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionStartDate"]) -> typing.Union[MetaOapg.properties.transactionStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unbilledReceivablesAccountingCode"]) -> typing.Union[MetaOapg.properties.unbilledReceivablesAccountingCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "UOM", "accountingCode", "adjustmentLiabilityAccountingCode", "adjustmentRevenueAccountingCode", "amountPerUnit", "billTargetDate", "billTo", "billToSnapshotId", "billingRule", "contractAssetAccountingCode", "contractLiabilityAccountingCode", "contractRecognizedRevenueAccountingCode", "currency", "customFields", "deferredRevenueAccountingCode", "discount", "excludeItemBillingFromRevenueAccounting", "excludeItemBookingFromRevenueAccounting", "inlineDiscountPerUnit", "inlineDiscountType", "invoiceOwnerAccountId", "invoiceOwnerAccountName", "invoiceOwnerAccountNumber", "isAllocationEligible", "isUnbilled", "itemCategory", "itemName", "itemState", "itemType", "listPrice", "listPricePerUnit", "originalOrderId", "originalOrderLineItemId", "originalOrderLineItemNumber", "originalOrderNumber", "ownerAccountId", "ownerAccountName", "ownerAccountNumber", "productCode", "productRatePlanChargeId", "purchaseOrderNumber", "quantity", "quantityAvailableForReturn", "quantityFulfilled", "quantityPendingFulfillment", "recognizedRevenueAccountingCode", "relatedSubscriptionNumber", "requiresFulfillment", "revenueRecognitionRule", "revenueRecognitionTiming", "revenueAmortizationMethod", "sequenceSetId", "soldTo", "soldToSnapshotId", "taxCode", "taxMode", "transactionEndDate", "transactionStartDate", "unbilledReceivablesAccountingCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        UOM: typing.Union[MetaOapg.properties.UOM, str, schemas.Unset] = schemas.unset,
        accountingCode: typing.Union[MetaOapg.properties.accountingCode, str, schemas.Unset] = schemas.unset,
        adjustmentLiabilityAccountingCode: typing.Union[MetaOapg.properties.adjustmentLiabilityAccountingCode, str, schemas.Unset] = schemas.unset,
        adjustmentRevenueAccountingCode: typing.Union[MetaOapg.properties.adjustmentRevenueAccountingCode, str, schemas.Unset] = schemas.unset,
        amountPerUnit: typing.Union[MetaOapg.properties.amountPerUnit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        billTargetDate: typing.Union[MetaOapg.properties.billTargetDate, str, date, schemas.Unset] = schemas.unset,
        billTo: typing.Union[MetaOapg.properties.billTo, str, schemas.Unset] = schemas.unset,
        billToSnapshotId: typing.Union[MetaOapg.properties.billToSnapshotId, str, schemas.Unset] = schemas.unset,
        billingRule: typing.Union[MetaOapg.properties.billingRule, str, schemas.Unset] = schemas.unset,
        contractAssetAccountingCode: typing.Union[MetaOapg.properties.contractAssetAccountingCode, str, schemas.Unset] = schemas.unset,
        contractLiabilityAccountingCode: typing.Union[MetaOapg.properties.contractLiabilityAccountingCode, str, schemas.Unset] = schemas.unset,
        contractRecognizedRevenueAccountingCode: typing.Union[MetaOapg.properties.contractRecognizedRevenueAccountingCode, str, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        customFields: typing.Union['OrderLineItemCustomFields', schemas.Unset] = schemas.unset,
        deferredRevenueAccountingCode: typing.Union[MetaOapg.properties.deferredRevenueAccountingCode, str, schemas.Unset] = schemas.unset,
        discount: typing.Union[MetaOapg.properties.discount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        excludeItemBillingFromRevenueAccounting: typing.Union[MetaOapg.properties.excludeItemBillingFromRevenueAccounting, bool, schemas.Unset] = schemas.unset,
        excludeItemBookingFromRevenueAccounting: typing.Union[MetaOapg.properties.excludeItemBookingFromRevenueAccounting, bool, schemas.Unset] = schemas.unset,
        inlineDiscountPerUnit: typing.Union[MetaOapg.properties.inlineDiscountPerUnit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        inlineDiscountType: typing.Union[MetaOapg.properties.inlineDiscountType, str, schemas.Unset] = schemas.unset,
        invoiceOwnerAccountId: typing.Union[MetaOapg.properties.invoiceOwnerAccountId, str, schemas.Unset] = schemas.unset,
        invoiceOwnerAccountName: typing.Union[MetaOapg.properties.invoiceOwnerAccountName, str, schemas.Unset] = schemas.unset,
        invoiceOwnerAccountNumber: typing.Union[MetaOapg.properties.invoiceOwnerAccountNumber, str, schemas.Unset] = schemas.unset,
        isAllocationEligible: typing.Union[MetaOapg.properties.isAllocationEligible, bool, schemas.Unset] = schemas.unset,
        isUnbilled: typing.Union[MetaOapg.properties.isUnbilled, bool, schemas.Unset] = schemas.unset,
        itemCategory: typing.Union[MetaOapg.properties.itemCategory, str, schemas.Unset] = schemas.unset,
        itemName: typing.Union[MetaOapg.properties.itemName, str, schemas.Unset] = schemas.unset,
        itemState: typing.Union[MetaOapg.properties.itemState, str, schemas.Unset] = schemas.unset,
        itemType: typing.Union[MetaOapg.properties.itemType, str, schemas.Unset] = schemas.unset,
        listPrice: typing.Union[MetaOapg.properties.listPrice, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        listPricePerUnit: typing.Union[MetaOapg.properties.listPricePerUnit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        originalOrderId: typing.Union[MetaOapg.properties.originalOrderId, str, schemas.Unset] = schemas.unset,
        originalOrderLineItemId: typing.Union[MetaOapg.properties.originalOrderLineItemId, str, schemas.Unset] = schemas.unset,
        originalOrderLineItemNumber: typing.Union[MetaOapg.properties.originalOrderLineItemNumber, str, schemas.Unset] = schemas.unset,
        originalOrderNumber: typing.Union[MetaOapg.properties.originalOrderNumber, str, schemas.Unset] = schemas.unset,
        ownerAccountId: typing.Union[MetaOapg.properties.ownerAccountId, str, schemas.Unset] = schemas.unset,
        ownerAccountName: typing.Union[MetaOapg.properties.ownerAccountName, str, schemas.Unset] = schemas.unset,
        ownerAccountNumber: typing.Union[MetaOapg.properties.ownerAccountNumber, str, schemas.Unset] = schemas.unset,
        productCode: typing.Union[MetaOapg.properties.productCode, str, schemas.Unset] = schemas.unset,
        productRatePlanChargeId: typing.Union[MetaOapg.properties.productRatePlanChargeId, str, schemas.Unset] = schemas.unset,
        purchaseOrderNumber: typing.Union[MetaOapg.properties.purchaseOrderNumber, str, schemas.Unset] = schemas.unset,
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        quantityAvailableForReturn: typing.Union[MetaOapg.properties.quantityAvailableForReturn, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        quantityFulfilled: typing.Union[MetaOapg.properties.quantityFulfilled, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        quantityPendingFulfillment: typing.Union[MetaOapg.properties.quantityPendingFulfillment, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        recognizedRevenueAccountingCode: typing.Union[MetaOapg.properties.recognizedRevenueAccountingCode, str, schemas.Unset] = schemas.unset,
        relatedSubscriptionNumber: typing.Union[MetaOapg.properties.relatedSubscriptionNumber, str, schemas.Unset] = schemas.unset,
        requiresFulfillment: typing.Union[MetaOapg.properties.requiresFulfillment, bool, schemas.Unset] = schemas.unset,
        revenueRecognitionRule: typing.Union[MetaOapg.properties.revenueRecognitionRule, str, schemas.Unset] = schemas.unset,
        revenueRecognitionTiming: typing.Union[MetaOapg.properties.revenueRecognitionTiming, str, schemas.Unset] = schemas.unset,
        revenueAmortizationMethod: typing.Union[MetaOapg.properties.revenueAmortizationMethod, str, schemas.Unset] = schemas.unset,
        sequenceSetId: typing.Union[MetaOapg.properties.sequenceSetId, str, schemas.Unset] = schemas.unset,
        soldTo: typing.Union[MetaOapg.properties.soldTo, str, schemas.Unset] = schemas.unset,
        soldToSnapshotId: typing.Union[MetaOapg.properties.soldToSnapshotId, str, schemas.Unset] = schemas.unset,
        taxCode: typing.Union[MetaOapg.properties.taxCode, str, schemas.Unset] = schemas.unset,
        taxMode: typing.Union[MetaOapg.properties.taxMode, str, schemas.Unset] = schemas.unset,
        transactionEndDate: typing.Union[MetaOapg.properties.transactionEndDate, str, date, schemas.Unset] = schemas.unset,
        transactionStartDate: typing.Union[MetaOapg.properties.transactionStartDate, str, date, schemas.Unset] = schemas.unset,
        unbilledReceivablesAccountingCode: typing.Union[MetaOapg.properties.unbilledReceivablesAccountingCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrderLineItemCommonRetrieveOrder':
        return super().__new__(
            cls,
            *args,
            description=description,
            UOM=UOM,
            accountingCode=accountingCode,
            adjustmentLiabilityAccountingCode=adjustmentLiabilityAccountingCode,
            adjustmentRevenueAccountingCode=adjustmentRevenueAccountingCode,
            amountPerUnit=amountPerUnit,
            billTargetDate=billTargetDate,
            billTo=billTo,
            billToSnapshotId=billToSnapshotId,
            billingRule=billingRule,
            contractAssetAccountingCode=contractAssetAccountingCode,
            contractLiabilityAccountingCode=contractLiabilityAccountingCode,
            contractRecognizedRevenueAccountingCode=contractRecognizedRevenueAccountingCode,
            currency=currency,
            customFields=customFields,
            deferredRevenueAccountingCode=deferredRevenueAccountingCode,
            discount=discount,
            excludeItemBillingFromRevenueAccounting=excludeItemBillingFromRevenueAccounting,
            excludeItemBookingFromRevenueAccounting=excludeItemBookingFromRevenueAccounting,
            inlineDiscountPerUnit=inlineDiscountPerUnit,
            inlineDiscountType=inlineDiscountType,
            invoiceOwnerAccountId=invoiceOwnerAccountId,
            invoiceOwnerAccountName=invoiceOwnerAccountName,
            invoiceOwnerAccountNumber=invoiceOwnerAccountNumber,
            isAllocationEligible=isAllocationEligible,
            isUnbilled=isUnbilled,
            itemCategory=itemCategory,
            itemName=itemName,
            itemState=itemState,
            itemType=itemType,
            listPrice=listPrice,
            listPricePerUnit=listPricePerUnit,
            originalOrderId=originalOrderId,
            originalOrderLineItemId=originalOrderLineItemId,
            originalOrderLineItemNumber=originalOrderLineItemNumber,
            originalOrderNumber=originalOrderNumber,
            ownerAccountId=ownerAccountId,
            ownerAccountName=ownerAccountName,
            ownerAccountNumber=ownerAccountNumber,
            productCode=productCode,
            productRatePlanChargeId=productRatePlanChargeId,
            purchaseOrderNumber=purchaseOrderNumber,
            quantity=quantity,
            quantityAvailableForReturn=quantityAvailableForReturn,
            quantityFulfilled=quantityFulfilled,
            quantityPendingFulfillment=quantityPendingFulfillment,
            recognizedRevenueAccountingCode=recognizedRevenueAccountingCode,
            relatedSubscriptionNumber=relatedSubscriptionNumber,
            requiresFulfillment=requiresFulfillment,
            revenueRecognitionRule=revenueRecognitionRule,
            revenueRecognitionTiming=revenueRecognitionTiming,
            revenueAmortizationMethod=revenueAmortizationMethod,
            sequenceSetId=sequenceSetId,
            soldTo=soldTo,
            soldToSnapshotId=soldToSnapshotId,
            taxCode=taxCode,
            taxMode=taxMode,
            transactionEndDate=transactionEndDate,
            transactionStartDate=transactionStartDate,
            unbilledReceivablesAccountingCode=unbilledReceivablesAccountingCode,
            _configuration=_configuration,
            **kwargs,
        )

from zuora_python_sdk.model.order_line_item_custom_fields import OrderLineItemCustomFields

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


class PostInvoiceResponse(
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
                    accountId = schemas.StrSchema
                    adjustmentAmount = schemas.DecimalSchema
                    amount = schemas.DecimalSchema
                    amountWithoutTax = schemas.DecimalSchema
                    autoPay = schemas.BoolSchema
                    balance = schemas.DecimalSchema
                    billRunId = schemas.StrSchema
                    billToContactId = schemas.StrSchema
                    billToContactSnapshotId = schemas.StrSchema
                    comments = schemas.StrSchema
                    createdById = schemas.StrSchema
                    createdDate = schemas.DateTimeSchema
                    creditBalanceAdjustmentAmount = schemas.DecimalSchema
                    creditMemoAmount = schemas.DecimalSchema
                    
                    
                    class currency(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'currency':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    discount = schemas.DecimalSchema
                    dueDate = schemas.DateSchema
                    einvoiceErrorCode = schemas.StrSchema
                    einvoiceErrorMessage = schemas.StrSchema
                    einvoiceFileId = schemas.StrSchema
                    
                    
                    class einvoiceStatus(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "Processing": "PROCESSING",
                                "Generated": "GENERATED",
                                "Success": "SUCCESS",
                                "Failed": "FAILED",
                            }
                        
                        @schemas.classproperty
                        def PROCESSING(cls):
                            return cls("Processing")
                        
                        @schemas.classproperty
                        def GENERATED(cls):
                            return cls("Generated")
                        
                        @schemas.classproperty
                        def SUCCESS(cls):
                            return cls("Success")
                        
                        @schemas.classproperty
                        def FAILED(cls):
                            return cls("Failed")
                    id = schemas.StrSchema
                    includesOneTime = schemas.BoolSchema
                    includesRecurring = schemas.BoolSchema
                    includesUsage = schemas.BoolSchema
                    invoiceDate = schemas.DateSchema
                    
                    
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
                    invoiceNumber = schemas.StrSchema
                    lastEmailSentDate = schemas.StrSchema
                    organizationLabel = schemas.StrSchema
                    paymentAmount = schemas.DecimalSchema
                    paymentTerm = schemas.StrSchema
                    postedBy = schemas.StrSchema
                    postedDate = schemas.DateSchema
                    refundAmount = schemas.DecimalSchema
                    sequenceSetId = schemas.StrSchema
                    soldToContactId = schemas.StrSchema
                    soldToContactSnapshotId = schemas.StrSchema
                    
                    
                    class source(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "BillRun": "BILL_RUN",
                                "API": "API",
                                "ApiSubscribe": "API_SUBSCRIBE",
                                "ApiAmend": "API_AMEND",
                            }
                        
                        @schemas.classproperty
                        def BILL_RUN(cls):
                            return cls("BillRun")
                        
                        @schemas.classproperty
                        def API(cls):
                            return cls("API")
                        
                        @schemas.classproperty
                        def API_SUBSCRIBE(cls):
                            return cls("ApiSubscribe")
                        
                        @schemas.classproperty
                        def API_AMEND(cls):
                            return cls("ApiAmend")
                    sourceId = schemas.StrSchema
                    
                    
                    class sourceType(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "Subscription": "SUBSCRIPTION",
                                "Standalone": "STANDALONE",
                                "Order": "ORDER",
                                "Consolidation": "CONSOLIDATION",
                            }
                        
                        @schemas.classproperty
                        def SUBSCRIPTION(cls):
                            return cls("Subscription")
                        
                        @schemas.classproperty
                        def STANDALONE(cls):
                            return cls("Standalone")
                        
                        @schemas.classproperty
                        def ORDER(cls):
                            return cls("Order")
                        
                        @schemas.classproperty
                        def CONSOLIDATION(cls):
                            return cls("Consolidation")
                    
                    
                    class status(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "Draft": "DRAFT",
                                "Posted": "POSTED",
                            }
                        
                        @schemas.classproperty
                        def DRAFT(cls):
                            return cls("Draft")
                        
                        @schemas.classproperty
                        def POSTED(cls):
                            return cls("Posted")
                    success = schemas.BoolSchema
                    targetDate = schemas.DateSchema
                    taxAmount = schemas.DecimalSchema
                    taxExemptAmount = schemas.DecimalSchema
                    taxMessage = schemas.StrSchema
                    
                    
                    class taxStatus(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "Complete": "COMPLETE",
                                "Error": "ERROR",
                                "UnknownError": "UNKNOWN_ERROR",
                                "DuplicateDoc": "DUPLICATE_DOC",
                                "InvalidRequest": "INVALID_REQUEST",
                                "InvalidResponse": "INVALID_RESPONSE",
                                "TaxEngineError": "TAX_ENGINE_ERROR",
                                "ConcurrentModify": "CONCURRENT_MODIFY",
                                "InternalServerError": "INTERNAL_SERVER_ERROR",
                                "TaxCodeTemplateError": "TAX_CODE_TEMPLATE_ERROR",
                            }
                        
                        @schemas.classproperty
                        def COMPLETE(cls):
                            return cls("Complete")
                        
                        @schemas.classproperty
                        def ERROR(cls):
                            return cls("Error")
                        
                        @schemas.classproperty
                        def UNKNOWN_ERROR(cls):
                            return cls("UnknownError")
                        
                        @schemas.classproperty
                        def DUPLICATE_DOC(cls):
                            return cls("DuplicateDoc")
                        
                        @schemas.classproperty
                        def INVALID_REQUEST(cls):
                            return cls("InvalidRequest")
                        
                        @schemas.classproperty
                        def INVALID_RESPONSE(cls):
                            return cls("InvalidResponse")
                        
                        @schemas.classproperty
                        def TAX_ENGINE_ERROR(cls):
                            return cls("TaxEngineError")
                        
                        @schemas.classproperty
                        def CONCURRENT_MODIFY(cls):
                            return cls("ConcurrentModify")
                        
                        @schemas.classproperty
                        def INTERNAL_SERVER_ERROR(cls):
                            return cls("InternalServerError")
                        
                        @schemas.classproperty
                        def TAX_CODE_TEMPLATE_ERROR(cls):
                            return cls("TaxCodeTemplateError")
                    templateId = schemas.StrSchema
                    
                    
                    class transferredToAccounting(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "Processing": "PROCESSING",
                                "Error": "ERROR",
                                "Ignore": "IGNORE",
                                "true": "TRUE",
                                "false": "FALSE",
                            }
                        
                        @schemas.classproperty
                        def PROCESSING(cls):
                            return cls("Processing")
                        
                        @schemas.classproperty
                        def ERROR(cls):
                            return cls("Error")
                        
                        @schemas.classproperty
                        def IGNORE(cls):
                            return cls("Ignore")
                        
                        @schemas.classproperty
                        def TRUE(cls):
                            return cls("true")
                        
                        @schemas.classproperty
                        def FALSE(cls):
                            return cls("false")
                    updatedById = schemas.StrSchema
                    updatedDate = schemas.DateTimeSchema
                    __annotations__ = {
                        "accountId": accountId,
                        "adjustmentAmount": adjustmentAmount,
                        "amount": amount,
                        "amountWithoutTax": amountWithoutTax,
                        "autoPay": autoPay,
                        "balance": balance,
                        "billRunId": billRunId,
                        "billToContactId": billToContactId,
                        "billToContactSnapshotId": billToContactSnapshotId,
                        "comments": comments,
                        "createdById": createdById,
                        "createdDate": createdDate,
                        "creditBalanceAdjustmentAmount": creditBalanceAdjustmentAmount,
                        "creditMemoAmount": creditMemoAmount,
                        "currency": currency,
                        "discount": discount,
                        "dueDate": dueDate,
                        "einvoiceErrorCode": einvoiceErrorCode,
                        "einvoiceErrorMessage": einvoiceErrorMessage,
                        "einvoiceFileId": einvoiceFileId,
                        "einvoiceStatus": einvoiceStatus,
                        "id": id,
                        "includesOneTime": includesOneTime,
                        "includesRecurring": includesRecurring,
                        "includesUsage": includesUsage,
                        "invoiceDate": invoiceDate,
                        "invoiceGroupNumber": invoiceGroupNumber,
                        "invoiceNumber": invoiceNumber,
                        "lastEmailSentDate": lastEmailSentDate,
                        "organizationLabel": organizationLabel,
                        "paymentAmount": paymentAmount,
                        "paymentTerm": paymentTerm,
                        "postedBy": postedBy,
                        "postedDate": postedDate,
                        "refundAmount": refundAmount,
                        "sequenceSetId": sequenceSetId,
                        "soldToContactId": soldToContactId,
                        "soldToContactSnapshotId": soldToContactSnapshotId,
                        "source": source,
                        "sourceId": sourceId,
                        "sourceType": sourceType,
                        "status": status,
                        "success": success,
                        "targetDate": targetDate,
                        "taxAmount": taxAmount,
                        "taxExemptAmount": taxExemptAmount,
                        "taxMessage": taxMessage,
                        "taxStatus": taxStatus,
                        "templateId": templateId,
                        "transferredToAccounting": transferredToAccounting,
                        "updatedById": updatedById,
                        "updatedDate": updatedDate,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["adjustmentAmount"]) -> MetaOapg.properties.adjustmentAmount: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["amountWithoutTax"]) -> MetaOapg.properties.amountWithoutTax: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["autoPay"]) -> MetaOapg.properties.autoPay: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["billRunId"]) -> MetaOapg.properties.billRunId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["billToContactId"]) -> MetaOapg.properties.billToContactId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["billToContactSnapshotId"]) -> MetaOapg.properties.billToContactSnapshotId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["createdById"]) -> MetaOapg.properties.createdById: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["creditBalanceAdjustmentAmount"]) -> MetaOapg.properties.creditBalanceAdjustmentAmount: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["creditMemoAmount"]) -> MetaOapg.properties.creditMemoAmount: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["discount"]) -> MetaOapg.properties.discount: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["dueDate"]) -> MetaOapg.properties.dueDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["einvoiceErrorCode"]) -> MetaOapg.properties.einvoiceErrorCode: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["einvoiceErrorMessage"]) -> MetaOapg.properties.einvoiceErrorMessage: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["einvoiceFileId"]) -> MetaOapg.properties.einvoiceFileId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["einvoiceStatus"]) -> MetaOapg.properties.einvoiceStatus: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["includesOneTime"]) -> MetaOapg.properties.includesOneTime: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["includesRecurring"]) -> MetaOapg.properties.includesRecurring: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["includesUsage"]) -> MetaOapg.properties.includesUsage: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceDate"]) -> MetaOapg.properties.invoiceDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceGroupNumber"]) -> MetaOapg.properties.invoiceGroupNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoiceNumber"]) -> MetaOapg.properties.invoiceNumber: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["lastEmailSentDate"]) -> MetaOapg.properties.lastEmailSentDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["organizationLabel"]) -> MetaOapg.properties.organizationLabel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["paymentAmount"]) -> MetaOapg.properties.paymentAmount: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["paymentTerm"]) -> MetaOapg.properties.paymentTerm: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["postedBy"]) -> MetaOapg.properties.postedBy: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["postedDate"]) -> MetaOapg.properties.postedDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["refundAmount"]) -> MetaOapg.properties.refundAmount: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sequenceSetId"]) -> MetaOapg.properties.sequenceSetId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["soldToContactId"]) -> MetaOapg.properties.soldToContactId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["soldToContactSnapshotId"]) -> MetaOapg.properties.soldToContactSnapshotId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sourceId"]) -> MetaOapg.properties.sourceId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sourceType"]) -> MetaOapg.properties.sourceType: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["targetDate"]) -> MetaOapg.properties.targetDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["taxAmount"]) -> MetaOapg.properties.taxAmount: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["taxExemptAmount"]) -> MetaOapg.properties.taxExemptAmount: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["taxMessage"]) -> MetaOapg.properties.taxMessage: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["taxStatus"]) -> MetaOapg.properties.taxStatus: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["transferredToAccounting"]) -> MetaOapg.properties.transferredToAccounting: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["updatedById"]) -> MetaOapg.properties.updatedById: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["updatedDate"]) -> MetaOapg.properties.updatedDate: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountId", "adjustmentAmount", "amount", "amountWithoutTax", "autoPay", "balance", "billRunId", "billToContactId", "billToContactSnapshotId", "comments", "createdById", "createdDate", "creditBalanceAdjustmentAmount", "creditMemoAmount", "currency", "discount", "dueDate", "einvoiceErrorCode", "einvoiceErrorMessage", "einvoiceFileId", "einvoiceStatus", "id", "includesOneTime", "includesRecurring", "includesUsage", "invoiceDate", "invoiceGroupNumber", "invoiceNumber", "lastEmailSentDate", "organizationLabel", "paymentAmount", "paymentTerm", "postedBy", "postedDate", "refundAmount", "sequenceSetId", "soldToContactId", "soldToContactSnapshotId", "source", "sourceId", "sourceType", "status", "success", "targetDate", "taxAmount", "taxExemptAmount", "taxMessage", "taxStatus", "templateId", "transferredToAccounting", "updatedById", "updatedDate", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> typing.Union[MetaOapg.properties.accountId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["adjustmentAmount"]) -> typing.Union[MetaOapg.properties.adjustmentAmount, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["amountWithoutTax"]) -> typing.Union[MetaOapg.properties.amountWithoutTax, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["autoPay"]) -> typing.Union[MetaOapg.properties.autoPay, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> typing.Union[MetaOapg.properties.balance, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["billRunId"]) -> typing.Union[MetaOapg.properties.billRunId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["billToContactId"]) -> typing.Union[MetaOapg.properties.billToContactId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["billToContactSnapshotId"]) -> typing.Union[MetaOapg.properties.billToContactSnapshotId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["createdById"]) -> typing.Union[MetaOapg.properties.createdById, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["createdDate"]) -> typing.Union[MetaOapg.properties.createdDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["creditBalanceAdjustmentAmount"]) -> typing.Union[MetaOapg.properties.creditBalanceAdjustmentAmount, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["creditMemoAmount"]) -> typing.Union[MetaOapg.properties.creditMemoAmount, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["discount"]) -> typing.Union[MetaOapg.properties.discount, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["dueDate"]) -> typing.Union[MetaOapg.properties.dueDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["einvoiceErrorCode"]) -> typing.Union[MetaOapg.properties.einvoiceErrorCode, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["einvoiceErrorMessage"]) -> typing.Union[MetaOapg.properties.einvoiceErrorMessage, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["einvoiceFileId"]) -> typing.Union[MetaOapg.properties.einvoiceFileId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["einvoiceStatus"]) -> typing.Union[MetaOapg.properties.einvoiceStatus, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["includesOneTime"]) -> typing.Union[MetaOapg.properties.includesOneTime, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["includesRecurring"]) -> typing.Union[MetaOapg.properties.includesRecurring, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["includesUsage"]) -> typing.Union[MetaOapg.properties.includesUsage, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceDate"]) -> typing.Union[MetaOapg.properties.invoiceDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceGroupNumber"]) -> typing.Union[MetaOapg.properties.invoiceGroupNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoiceNumber"]) -> typing.Union[MetaOapg.properties.invoiceNumber, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["lastEmailSentDate"]) -> typing.Union[MetaOapg.properties.lastEmailSentDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["organizationLabel"]) -> typing.Union[MetaOapg.properties.organizationLabel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["paymentAmount"]) -> typing.Union[MetaOapg.properties.paymentAmount, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["paymentTerm"]) -> typing.Union[MetaOapg.properties.paymentTerm, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["postedBy"]) -> typing.Union[MetaOapg.properties.postedBy, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["postedDate"]) -> typing.Union[MetaOapg.properties.postedDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["refundAmount"]) -> typing.Union[MetaOapg.properties.refundAmount, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sequenceSetId"]) -> typing.Union[MetaOapg.properties.sequenceSetId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["soldToContactId"]) -> typing.Union[MetaOapg.properties.soldToContactId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["soldToContactSnapshotId"]) -> typing.Union[MetaOapg.properties.soldToContactSnapshotId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sourceId"]) -> typing.Union[MetaOapg.properties.sourceId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sourceType"]) -> typing.Union[MetaOapg.properties.sourceType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> typing.Union[MetaOapg.properties.success, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["targetDate"]) -> typing.Union[MetaOapg.properties.targetDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["taxAmount"]) -> typing.Union[MetaOapg.properties.taxAmount, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["taxExemptAmount"]) -> typing.Union[MetaOapg.properties.taxExemptAmount, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["taxMessage"]) -> typing.Union[MetaOapg.properties.taxMessage, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["taxStatus"]) -> typing.Union[MetaOapg.properties.taxStatus, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["templateId"]) -> typing.Union[MetaOapg.properties.templateId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["transferredToAccounting"]) -> typing.Union[MetaOapg.properties.transferredToAccounting, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["updatedById"]) -> typing.Union[MetaOapg.properties.updatedById, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["updatedDate"]) -> typing.Union[MetaOapg.properties.updatedDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountId", "adjustmentAmount", "amount", "amountWithoutTax", "autoPay", "balance", "billRunId", "billToContactId", "billToContactSnapshotId", "comments", "createdById", "createdDate", "creditBalanceAdjustmentAmount", "creditMemoAmount", "currency", "discount", "dueDate", "einvoiceErrorCode", "einvoiceErrorMessage", "einvoiceFileId", "einvoiceStatus", "id", "includesOneTime", "includesRecurring", "includesUsage", "invoiceDate", "invoiceGroupNumber", "invoiceNumber", "lastEmailSentDate", "organizationLabel", "paymentAmount", "paymentTerm", "postedBy", "postedDate", "refundAmount", "sequenceSetId", "soldToContactId", "soldToContactSnapshotId", "source", "sourceId", "sourceType", "status", "success", "targetDate", "taxAmount", "taxExemptAmount", "taxMessage", "taxStatus", "templateId", "transferredToAccounting", "updatedById", "updatedDate", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                accountId: typing.Union[MetaOapg.properties.accountId, str, schemas.Unset] = schemas.unset,
                adjustmentAmount: typing.Union[MetaOapg.properties.adjustmentAmount, str, schemas.Unset] = schemas.unset,
                amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
                amountWithoutTax: typing.Union[MetaOapg.properties.amountWithoutTax, str, schemas.Unset] = schemas.unset,
                autoPay: typing.Union[MetaOapg.properties.autoPay, bool, schemas.Unset] = schemas.unset,
                balance: typing.Union[MetaOapg.properties.balance, str, schemas.Unset] = schemas.unset,
                billRunId: typing.Union[MetaOapg.properties.billRunId, str, schemas.Unset] = schemas.unset,
                billToContactId: typing.Union[MetaOapg.properties.billToContactId, str, schemas.Unset] = schemas.unset,
                billToContactSnapshotId: typing.Union[MetaOapg.properties.billToContactSnapshotId, str, schemas.Unset] = schemas.unset,
                comments: typing.Union[MetaOapg.properties.comments, str, schemas.Unset] = schemas.unset,
                createdById: typing.Union[MetaOapg.properties.createdById, str, schemas.Unset] = schemas.unset,
                createdDate: typing.Union[MetaOapg.properties.createdDate, str, datetime, schemas.Unset] = schemas.unset,
                creditBalanceAdjustmentAmount: typing.Union[MetaOapg.properties.creditBalanceAdjustmentAmount, str, schemas.Unset] = schemas.unset,
                creditMemoAmount: typing.Union[MetaOapg.properties.creditMemoAmount, str, schemas.Unset] = schemas.unset,
                currency: typing.Union[MetaOapg.properties.currency, None, str, schemas.Unset] = schemas.unset,
                discount: typing.Union[MetaOapg.properties.discount, str, schemas.Unset] = schemas.unset,
                dueDate: typing.Union[MetaOapg.properties.dueDate, str, date, schemas.Unset] = schemas.unset,
                einvoiceErrorCode: typing.Union[MetaOapg.properties.einvoiceErrorCode, str, schemas.Unset] = schemas.unset,
                einvoiceErrorMessage: typing.Union[MetaOapg.properties.einvoiceErrorMessage, str, schemas.Unset] = schemas.unset,
                einvoiceFileId: typing.Union[MetaOapg.properties.einvoiceFileId, str, schemas.Unset] = schemas.unset,
                einvoiceStatus: typing.Union[MetaOapg.properties.einvoiceStatus, str, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                includesOneTime: typing.Union[MetaOapg.properties.includesOneTime, bool, schemas.Unset] = schemas.unset,
                includesRecurring: typing.Union[MetaOapg.properties.includesRecurring, bool, schemas.Unset] = schemas.unset,
                includesUsage: typing.Union[MetaOapg.properties.includesUsage, bool, schemas.Unset] = schemas.unset,
                invoiceDate: typing.Union[MetaOapg.properties.invoiceDate, str, date, schemas.Unset] = schemas.unset,
                invoiceGroupNumber: typing.Union[MetaOapg.properties.invoiceGroupNumber, None, str, schemas.Unset] = schemas.unset,
                invoiceNumber: typing.Union[MetaOapg.properties.invoiceNumber, str, schemas.Unset] = schemas.unset,
                lastEmailSentDate: typing.Union[MetaOapg.properties.lastEmailSentDate, str, schemas.Unset] = schemas.unset,
                organizationLabel: typing.Union[MetaOapg.properties.organizationLabel, str, schemas.Unset] = schemas.unset,
                paymentAmount: typing.Union[MetaOapg.properties.paymentAmount, str, schemas.Unset] = schemas.unset,
                paymentTerm: typing.Union[MetaOapg.properties.paymentTerm, str, schemas.Unset] = schemas.unset,
                postedBy: typing.Union[MetaOapg.properties.postedBy, str, schemas.Unset] = schemas.unset,
                postedDate: typing.Union[MetaOapg.properties.postedDate, str, date, schemas.Unset] = schemas.unset,
                refundAmount: typing.Union[MetaOapg.properties.refundAmount, str, schemas.Unset] = schemas.unset,
                sequenceSetId: typing.Union[MetaOapg.properties.sequenceSetId, str, schemas.Unset] = schemas.unset,
                soldToContactId: typing.Union[MetaOapg.properties.soldToContactId, str, schemas.Unset] = schemas.unset,
                soldToContactSnapshotId: typing.Union[MetaOapg.properties.soldToContactSnapshotId, str, schemas.Unset] = schemas.unset,
                source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
                sourceId: typing.Union[MetaOapg.properties.sourceId, str, schemas.Unset] = schemas.unset,
                sourceType: typing.Union[MetaOapg.properties.sourceType, str, schemas.Unset] = schemas.unset,
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                success: typing.Union[MetaOapg.properties.success, bool, schemas.Unset] = schemas.unset,
                targetDate: typing.Union[MetaOapg.properties.targetDate, str, date, schemas.Unset] = schemas.unset,
                taxAmount: typing.Union[MetaOapg.properties.taxAmount, str, schemas.Unset] = schemas.unset,
                taxExemptAmount: typing.Union[MetaOapg.properties.taxExemptAmount, str, schemas.Unset] = schemas.unset,
                taxMessage: typing.Union[MetaOapg.properties.taxMessage, str, schemas.Unset] = schemas.unset,
                taxStatus: typing.Union[MetaOapg.properties.taxStatus, str, schemas.Unset] = schemas.unset,
                templateId: typing.Union[MetaOapg.properties.templateId, str, schemas.Unset] = schemas.unset,
                transferredToAccounting: typing.Union[MetaOapg.properties.transferredToAccounting, str, schemas.Unset] = schemas.unset,
                updatedById: typing.Union[MetaOapg.properties.updatedById, str, schemas.Unset] = schemas.unset,
                updatedDate: typing.Union[MetaOapg.properties.updatedDate, str, datetime, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    accountId=accountId,
                    adjustmentAmount=adjustmentAmount,
                    amount=amount,
                    amountWithoutTax=amountWithoutTax,
                    autoPay=autoPay,
                    balance=balance,
                    billRunId=billRunId,
                    billToContactId=billToContactId,
                    billToContactSnapshotId=billToContactSnapshotId,
                    comments=comments,
                    createdById=createdById,
                    createdDate=createdDate,
                    creditBalanceAdjustmentAmount=creditBalanceAdjustmentAmount,
                    creditMemoAmount=creditMemoAmount,
                    currency=currency,
                    discount=discount,
                    dueDate=dueDate,
                    einvoiceErrorCode=einvoiceErrorCode,
                    einvoiceErrorMessage=einvoiceErrorMessage,
                    einvoiceFileId=einvoiceFileId,
                    einvoiceStatus=einvoiceStatus,
                    id=id,
                    includesOneTime=includesOneTime,
                    includesRecurring=includesRecurring,
                    includesUsage=includesUsage,
                    invoiceDate=invoiceDate,
                    invoiceGroupNumber=invoiceGroupNumber,
                    invoiceNumber=invoiceNumber,
                    lastEmailSentDate=lastEmailSentDate,
                    organizationLabel=organizationLabel,
                    paymentAmount=paymentAmount,
                    paymentTerm=paymentTerm,
                    postedBy=postedBy,
                    postedDate=postedDate,
                    refundAmount=refundAmount,
                    sequenceSetId=sequenceSetId,
                    soldToContactId=soldToContactId,
                    soldToContactSnapshotId=soldToContactSnapshotId,
                    source=source,
                    sourceId=sourceId,
                    sourceType=sourceType,
                    status=status,
                    success=success,
                    targetDate=targetDate,
                    taxAmount=taxAmount,
                    taxExemptAmount=taxExemptAmount,
                    taxMessage=taxMessage,
                    taxStatus=taxStatus,
                    templateId=templateId,
                    transferredToAccounting=transferredToAccounting,
                    updatedById=updatedById,
                    updatedDate=updatedDate,
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
                InvoiceObjectNSFields,
                InvoiceObjectCustomFields,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostInvoiceResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from zuora_python_sdk.model.invoice_object_custom_fields import InvoiceObjectCustomFields
from zuora_python_sdk.model.invoice_object_ns_fields import InvoiceObjectNSFields

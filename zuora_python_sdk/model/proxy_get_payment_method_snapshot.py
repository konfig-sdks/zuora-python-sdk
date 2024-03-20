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


class ProxyGetPaymentMethodSnapshot(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            AccountId = schemas.StrSchema
            AchAbaCode = schemas.StrSchema
            AchAccountName = schemas.StrSchema
            AchAccountNumberMask = schemas.StrSchema
            
            
            class AchAccountType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "BusinessChecking": "BUSINESS_CHECKING",
                        "Checking": "CHECKING",
                        "Saving": "SAVING",
                    }
                
                @schemas.classproperty
                def BUSINESS_CHECKING(cls):
                    return cls("BusinessChecking")
                
                @schemas.classproperty
                def CHECKING(cls):
                    return cls("Checking")
                
                @schemas.classproperty
                def SAVING(cls):
                    return cls("Saving")
            AchBankName = schemas.StrSchema
            BankBranchCode = schemas.StrSchema
            BankCheckDigit = schemas.StrSchema
            BankCity = schemas.StrSchema
            BankCode = schemas.StrSchema
            BankIdentificationNumber = schemas.StrSchema
            BankName = schemas.StrSchema
            BankPostalCode = schemas.StrSchema
            BankStreetName = schemas.StrSchema
            BankStreetNumber = schemas.StrSchema
            BankTransferAccountName = schemas.StrSchema
            BankTransferAccountNumberMask = schemas.StrSchema
            BankTransferAccountType = schemas.StrSchema
            
            
            class BankTransferType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "AutomatischIncasso": "AUTOMATISCH_INCASSO",
                        "LastschriftDE": "LASTSCHRIFT_DE",
                        "LastschriftAT": "LASTSCHRIFT_AT",
                        "DemandeDePrelevement": "DEMANDE_DE_PRELEVEMENT",
                        "DirectDebitUK": "DIRECT_DEBIT_UK",
                        "Domicil": "DOMICIL",
                        "LastschriftCH": "LASTSCHRIFT_CH",
                        "RID": "RID",
                        "OrdenDeDomiciliacion": "ORDEN_DE_DOMICILIACION",
                        "Autogiro": "AUTOGIRO",
                        "Betalingsservice": "BETALINGSSERVICE",
                    }
                
                @schemas.classproperty
                def AUTOMATISCH_INCASSO(cls):
                    return cls("AutomatischIncasso")
                
                @schemas.classproperty
                def LASTSCHRIFT_DE(cls):
                    return cls("LastschriftDE")
                
                @schemas.classproperty
                def LASTSCHRIFT_AT(cls):
                    return cls("LastschriftAT")
                
                @schemas.classproperty
                def DEMANDE_DE_PRELEVEMENT(cls):
                    return cls("DemandeDePrelevement")
                
                @schemas.classproperty
                def DIRECT_DEBIT_UK(cls):
                    return cls("DirectDebitUK")
                
                @schemas.classproperty
                def DOMICIL(cls):
                    return cls("Domicil")
                
                @schemas.classproperty
                def LASTSCHRIFT_CH(cls):
                    return cls("LastschriftCH")
                
                @schemas.classproperty
                def RID(cls):
                    return cls("RID")
                
                @schemas.classproperty
                def ORDEN_DE_DOMICILIACION(cls):
                    return cls("OrdenDeDomiciliacion")
                
                @schemas.classproperty
                def AUTOGIRO(cls):
                    return cls("Autogiro")
                
                @schemas.classproperty
                def BETALINGSSERVICE(cls):
                    return cls("Betalingsservice")
            BusinessIdentificationCode = schemas.StrSchema
            City = schemas.StrSchema
            CompanyName = schemas.StrSchema
            Country = schemas.StrSchema
            CreditCardAddress1 = schemas.StrSchema
            CreditCardAddress2 = schemas.StrSchema
            CreditCardCity = schemas.StrSchema
            CreditCardCountry = schemas.StrSchema
            CreditCardExpirationMonth = schemas.Int32Schema
            CreditCardExpirationYear = schemas.Int32Schema
            CreditCardHolderName = schemas.StrSchema
            CreditCardMaskNumber = schemas.StrSchema
            CreditCardPostalCode = schemas.StrSchema
            CreditCardState = schemas.StrSchema
            
            
            class CreditCardType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "AmericanExpress": "AMERICAN_EXPRESS",
                        "Discover": "DISCOVER",
                        "MasterCard": "MASTER_CARD",
                        "Visa": "VISA",
                    }
                
                @schemas.classproperty
                def AMERICAN_EXPRESS(cls):
                    return cls("AmericanExpress")
                
                @schemas.classproperty
                def DISCOVER(cls):
                    return cls("Discover")
                
                @schemas.classproperty
                def MASTER_CARD(cls):
                    return cls("MasterCard")
                
                @schemas.classproperty
                def VISA(cls):
                    return cls("Visa")
            DeviceSessionId = schemas.StrSchema
            Email = schemas.StrSchema
            
            
            class ExistingMandate(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "true": "TRUE",
                        "false": "FALSE",
                    }
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls("true")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
            FirstName = schemas.StrSchema
            IBAN = schemas.StrSchema
            IPAddress = schemas.StrSchema
            Id = schemas.StrSchema
            IdentityNumber = schemas.StrSchema
            IsCompany = schemas.BoolSchema
            LastFailedSaleTransactionDate = schemas.DateTimeSchema
            LastName = schemas.StrSchema
            LastTransactionDateTime = schemas.DateTimeSchema
            LastTransactionStatus = schemas.StrSchema
            MandateCreationDate = schemas.DateSchema
            MandateID = schemas.StrSchema
            MandateReceived = schemas.StrSchema
            MandateUpdateDate = schemas.DateSchema
            MaxConsecutivePaymentFailures = schemas.IntSchema
            Name = schemas.StrSchema
            NumConsecutiveFailures = schemas.Int32Schema
            PaymentMethodId = schemas.StrSchema
            
            
            class PaymentMethodStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Active": "ACTIVE",
                        "Closed": "CLOSED",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("Active")
                
                @schemas.classproperty
                def CLOSED(cls):
                    return cls("Closed")
            PaymentRetryWindow = schemas.IntSchema
            PaypalBaid = schemas.StrSchema
            PaypalEmail = schemas.StrSchema
            PaypalPreapprovalKey = schemas.StrSchema
            
            
            class PaypalType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ExpressCheckout": "EXPRESS_CHECKOUT",
                        "AdaptivePayments": "ADAPTIVE_PAYMENTS",
                    }
                
                @schemas.classproperty
                def EXPRESS_CHECKOUT(cls):
                    return cls("ExpressCheckout")
                
                @schemas.classproperty
                def ADAPTIVE_PAYMENTS(cls):
                    return cls("AdaptivePayments")
            Phone = schemas.StrSchema
            PostalCode = schemas.StrSchema
            SecondTokenId = schemas.StrSchema
            State = schemas.StrSchema
            StreetName = schemas.StrSchema
            StreetNumber = schemas.StrSchema
            TokenId = schemas.StrSchema
            TotalNumberOfErrorPayments = schemas.Int32Schema
            TotalNumberOfProcessedPayments = schemas.Int32Schema
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ACH": "ACH",
                        "ApplePay": "APPLE_PAY",
                        "BankTransfer": "BANK_TRANSFER",
                        "Cash": "CASH",
                        "Check": "CHECK",
                        "CreditCard": "CREDIT_CARD",
                        "CreditCardReferenceTransaction": "CREDIT_CARD_REFERENCE_TRANSACTION",
                        "DebitCard": "DEBIT_CARD",
                        "Other": "OTHER",
                        "PayPal": "PAY_PAL",
                        "WireTransfer": "WIRE_TRANSFER",
                    }
                
                @schemas.classproperty
                def ACH(cls):
                    return cls("ACH")
                
                @schemas.classproperty
                def APPLE_PAY(cls):
                    return cls("ApplePay")
                
                @schemas.classproperty
                def BANK_TRANSFER(cls):
                    return cls("BankTransfer")
                
                @schemas.classproperty
                def CASH(cls):
                    return cls("Cash")
                
                @schemas.classproperty
                def CHECK(cls):
                    return cls("Check")
                
                @schemas.classproperty
                def CREDIT_CARD(cls):
                    return cls("CreditCard")
                
                @schemas.classproperty
                def CREDIT_CARD_REFERENCE_TRANSACTION(cls):
                    return cls("CreditCardReferenceTransaction")
                
                @schemas.classproperty
                def DEBIT_CARD(cls):
                    return cls("DebitCard")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def PAY_PAL(cls):
                    return cls("PayPal")
                
                @schemas.classproperty
                def WIRE_TRANSFER(cls):
                    return cls("WireTransfer")
            UseDefaultRetryRule = schemas.BoolSchema
            __annotations__ = {
                "AccountId": AccountId,
                "AchAbaCode": AchAbaCode,
                "AchAccountName": AchAccountName,
                "AchAccountNumberMask": AchAccountNumberMask,
                "AchAccountType": AchAccountType,
                "AchBankName": AchBankName,
                "BankBranchCode": BankBranchCode,
                "BankCheckDigit": BankCheckDigit,
                "BankCity": BankCity,
                "BankCode": BankCode,
                "BankIdentificationNumber": BankIdentificationNumber,
                "BankName": BankName,
                "BankPostalCode": BankPostalCode,
                "BankStreetName": BankStreetName,
                "BankStreetNumber": BankStreetNumber,
                "BankTransferAccountName": BankTransferAccountName,
                "BankTransferAccountNumberMask": BankTransferAccountNumberMask,
                "BankTransferAccountType": BankTransferAccountType,
                "BankTransferType": BankTransferType,
                "BusinessIdentificationCode": BusinessIdentificationCode,
                "City": City,
                "CompanyName": CompanyName,
                "Country": Country,
                "CreditCardAddress1": CreditCardAddress1,
                "CreditCardAddress2": CreditCardAddress2,
                "CreditCardCity": CreditCardCity,
                "CreditCardCountry": CreditCardCountry,
                "CreditCardExpirationMonth": CreditCardExpirationMonth,
                "CreditCardExpirationYear": CreditCardExpirationYear,
                "CreditCardHolderName": CreditCardHolderName,
                "CreditCardMaskNumber": CreditCardMaskNumber,
                "CreditCardPostalCode": CreditCardPostalCode,
                "CreditCardState": CreditCardState,
                "CreditCardType": CreditCardType,
                "DeviceSessionId": DeviceSessionId,
                "Email": Email,
                "ExistingMandate": ExistingMandate,
                "FirstName": FirstName,
                "IBAN": IBAN,
                "IPAddress": IPAddress,
                "Id": Id,
                "IdentityNumber": IdentityNumber,
                "IsCompany": IsCompany,
                "LastFailedSaleTransactionDate": LastFailedSaleTransactionDate,
                "LastName": LastName,
                "LastTransactionDateTime": LastTransactionDateTime,
                "LastTransactionStatus": LastTransactionStatus,
                "MandateCreationDate": MandateCreationDate,
                "MandateID": MandateID,
                "MandateReceived": MandateReceived,
                "MandateUpdateDate": MandateUpdateDate,
                "MaxConsecutivePaymentFailures": MaxConsecutivePaymentFailures,
                "Name": Name,
                "NumConsecutiveFailures": NumConsecutiveFailures,
                "PaymentMethodId": PaymentMethodId,
                "PaymentMethodStatus": PaymentMethodStatus,
                "PaymentRetryWindow": PaymentRetryWindow,
                "PaypalBaid": PaypalBaid,
                "PaypalEmail": PaypalEmail,
                "PaypalPreapprovalKey": PaypalPreapprovalKey,
                "PaypalType": PaypalType,
                "Phone": Phone,
                "PostalCode": PostalCode,
                "SecondTokenId": SecondTokenId,
                "State": State,
                "StreetName": StreetName,
                "StreetNumber": StreetNumber,
                "TokenId": TokenId,
                "TotalNumberOfErrorPayments": TotalNumberOfErrorPayments,
                "TotalNumberOfProcessedPayments": TotalNumberOfProcessedPayments,
                "Type": Type,
                "UseDefaultRetryRule": UseDefaultRetryRule,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> MetaOapg.properties.AccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AchAbaCode"]) -> MetaOapg.properties.AchAbaCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AchAccountName"]) -> MetaOapg.properties.AchAccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AchAccountNumberMask"]) -> MetaOapg.properties.AchAccountNumberMask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AchAccountType"]) -> MetaOapg.properties.AchAccountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AchBankName"]) -> MetaOapg.properties.AchBankName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankBranchCode"]) -> MetaOapg.properties.BankBranchCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankCheckDigit"]) -> MetaOapg.properties.BankCheckDigit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankCity"]) -> MetaOapg.properties.BankCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankCode"]) -> MetaOapg.properties.BankCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankIdentificationNumber"]) -> MetaOapg.properties.BankIdentificationNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankName"]) -> MetaOapg.properties.BankName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankPostalCode"]) -> MetaOapg.properties.BankPostalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankStreetName"]) -> MetaOapg.properties.BankStreetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankStreetNumber"]) -> MetaOapg.properties.BankStreetNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankTransferAccountName"]) -> MetaOapg.properties.BankTransferAccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankTransferAccountNumberMask"]) -> MetaOapg.properties.BankTransferAccountNumberMask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankTransferAccountType"]) -> MetaOapg.properties.BankTransferAccountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankTransferType"]) -> MetaOapg.properties.BankTransferType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BusinessIdentificationCode"]) -> MetaOapg.properties.BusinessIdentificationCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["City"]) -> MetaOapg.properties.City: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CompanyName"]) -> MetaOapg.properties.CompanyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Country"]) -> MetaOapg.properties.Country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardAddress1"]) -> MetaOapg.properties.CreditCardAddress1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardAddress2"]) -> MetaOapg.properties.CreditCardAddress2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardCity"]) -> MetaOapg.properties.CreditCardCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardCountry"]) -> MetaOapg.properties.CreditCardCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardExpirationMonth"]) -> MetaOapg.properties.CreditCardExpirationMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardExpirationYear"]) -> MetaOapg.properties.CreditCardExpirationYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardHolderName"]) -> MetaOapg.properties.CreditCardHolderName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardMaskNumber"]) -> MetaOapg.properties.CreditCardMaskNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardPostalCode"]) -> MetaOapg.properties.CreditCardPostalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardState"]) -> MetaOapg.properties.CreditCardState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditCardType"]) -> MetaOapg.properties.CreditCardType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DeviceSessionId"]) -> MetaOapg.properties.DeviceSessionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Email"]) -> MetaOapg.properties.Email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExistingMandate"]) -> MetaOapg.properties.ExistingMandate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IBAN"]) -> MetaOapg.properties.IBAN: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IPAddress"]) -> MetaOapg.properties.IPAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IdentityNumber"]) -> MetaOapg.properties.IdentityNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsCompany"]) -> MetaOapg.properties.IsCompany: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastFailedSaleTransactionDate"]) -> MetaOapg.properties.LastFailedSaleTransactionDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastTransactionDateTime"]) -> MetaOapg.properties.LastTransactionDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastTransactionStatus"]) -> MetaOapg.properties.LastTransactionStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MandateCreationDate"]) -> MetaOapg.properties.MandateCreationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MandateID"]) -> MetaOapg.properties.MandateID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MandateReceived"]) -> MetaOapg.properties.MandateReceived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MandateUpdateDate"]) -> MetaOapg.properties.MandateUpdateDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MaxConsecutivePaymentFailures"]) -> MetaOapg.properties.MaxConsecutivePaymentFailures: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NumConsecutiveFailures"]) -> MetaOapg.properties.NumConsecutiveFailures: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaymentMethodId"]) -> MetaOapg.properties.PaymentMethodId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaymentMethodStatus"]) -> MetaOapg.properties.PaymentMethodStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaymentRetryWindow"]) -> MetaOapg.properties.PaymentRetryWindow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaypalBaid"]) -> MetaOapg.properties.PaypalBaid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaypalEmail"]) -> MetaOapg.properties.PaypalEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaypalPreapprovalKey"]) -> MetaOapg.properties.PaypalPreapprovalKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaypalType"]) -> MetaOapg.properties.PaypalType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Phone"]) -> MetaOapg.properties.Phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PostalCode"]) -> MetaOapg.properties.PostalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SecondTokenId"]) -> MetaOapg.properties.SecondTokenId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["State"]) -> MetaOapg.properties.State: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StreetName"]) -> MetaOapg.properties.StreetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StreetNumber"]) -> MetaOapg.properties.StreetNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TokenId"]) -> MetaOapg.properties.TokenId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalNumberOfErrorPayments"]) -> MetaOapg.properties.TotalNumberOfErrorPayments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalNumberOfProcessedPayments"]) -> MetaOapg.properties.TotalNumberOfProcessedPayments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UseDefaultRetryRule"]) -> MetaOapg.properties.UseDefaultRetryRule: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "AchAbaCode", "AchAccountName", "AchAccountNumberMask", "AchAccountType", "AchBankName", "BankBranchCode", "BankCheckDigit", "BankCity", "BankCode", "BankIdentificationNumber", "BankName", "BankPostalCode", "BankStreetName", "BankStreetNumber", "BankTransferAccountName", "BankTransferAccountNumberMask", "BankTransferAccountType", "BankTransferType", "BusinessIdentificationCode", "City", "CompanyName", "Country", "CreditCardAddress1", "CreditCardAddress2", "CreditCardCity", "CreditCardCountry", "CreditCardExpirationMonth", "CreditCardExpirationYear", "CreditCardHolderName", "CreditCardMaskNumber", "CreditCardPostalCode", "CreditCardState", "CreditCardType", "DeviceSessionId", "Email", "ExistingMandate", "FirstName", "IBAN", "IPAddress", "Id", "IdentityNumber", "IsCompany", "LastFailedSaleTransactionDate", "LastName", "LastTransactionDateTime", "LastTransactionStatus", "MandateCreationDate", "MandateID", "MandateReceived", "MandateUpdateDate", "MaxConsecutivePaymentFailures", "Name", "NumConsecutiveFailures", "PaymentMethodId", "PaymentMethodStatus", "PaymentRetryWindow", "PaypalBaid", "PaypalEmail", "PaypalPreapprovalKey", "PaypalType", "Phone", "PostalCode", "SecondTokenId", "State", "StreetName", "StreetNumber", "TokenId", "TotalNumberOfErrorPayments", "TotalNumberOfProcessedPayments", "Type", "UseDefaultRetryRule", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> typing.Union[MetaOapg.properties.AccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AchAbaCode"]) -> typing.Union[MetaOapg.properties.AchAbaCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AchAccountName"]) -> typing.Union[MetaOapg.properties.AchAccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AchAccountNumberMask"]) -> typing.Union[MetaOapg.properties.AchAccountNumberMask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AchAccountType"]) -> typing.Union[MetaOapg.properties.AchAccountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AchBankName"]) -> typing.Union[MetaOapg.properties.AchBankName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankBranchCode"]) -> typing.Union[MetaOapg.properties.BankBranchCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankCheckDigit"]) -> typing.Union[MetaOapg.properties.BankCheckDigit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankCity"]) -> typing.Union[MetaOapg.properties.BankCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankCode"]) -> typing.Union[MetaOapg.properties.BankCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankIdentificationNumber"]) -> typing.Union[MetaOapg.properties.BankIdentificationNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankName"]) -> typing.Union[MetaOapg.properties.BankName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankPostalCode"]) -> typing.Union[MetaOapg.properties.BankPostalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankStreetName"]) -> typing.Union[MetaOapg.properties.BankStreetName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankStreetNumber"]) -> typing.Union[MetaOapg.properties.BankStreetNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankTransferAccountName"]) -> typing.Union[MetaOapg.properties.BankTransferAccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankTransferAccountNumberMask"]) -> typing.Union[MetaOapg.properties.BankTransferAccountNumberMask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankTransferAccountType"]) -> typing.Union[MetaOapg.properties.BankTransferAccountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankTransferType"]) -> typing.Union[MetaOapg.properties.BankTransferType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BusinessIdentificationCode"]) -> typing.Union[MetaOapg.properties.BusinessIdentificationCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["City"]) -> typing.Union[MetaOapg.properties.City, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CompanyName"]) -> typing.Union[MetaOapg.properties.CompanyName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Country"]) -> typing.Union[MetaOapg.properties.Country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardAddress1"]) -> typing.Union[MetaOapg.properties.CreditCardAddress1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardAddress2"]) -> typing.Union[MetaOapg.properties.CreditCardAddress2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardCity"]) -> typing.Union[MetaOapg.properties.CreditCardCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardCountry"]) -> typing.Union[MetaOapg.properties.CreditCardCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardExpirationMonth"]) -> typing.Union[MetaOapg.properties.CreditCardExpirationMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardExpirationYear"]) -> typing.Union[MetaOapg.properties.CreditCardExpirationYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardHolderName"]) -> typing.Union[MetaOapg.properties.CreditCardHolderName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardMaskNumber"]) -> typing.Union[MetaOapg.properties.CreditCardMaskNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardPostalCode"]) -> typing.Union[MetaOapg.properties.CreditCardPostalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardState"]) -> typing.Union[MetaOapg.properties.CreditCardState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditCardType"]) -> typing.Union[MetaOapg.properties.CreditCardType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DeviceSessionId"]) -> typing.Union[MetaOapg.properties.DeviceSessionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union[MetaOapg.properties.Email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExistingMandate"]) -> typing.Union[MetaOapg.properties.ExistingMandate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstName"]) -> typing.Union[MetaOapg.properties.FirstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IBAN"]) -> typing.Union[MetaOapg.properties.IBAN, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IPAddress"]) -> typing.Union[MetaOapg.properties.IPAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IdentityNumber"]) -> typing.Union[MetaOapg.properties.IdentityNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsCompany"]) -> typing.Union[MetaOapg.properties.IsCompany, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastFailedSaleTransactionDate"]) -> typing.Union[MetaOapg.properties.LastFailedSaleTransactionDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastName"]) -> typing.Union[MetaOapg.properties.LastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastTransactionDateTime"]) -> typing.Union[MetaOapg.properties.LastTransactionDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastTransactionStatus"]) -> typing.Union[MetaOapg.properties.LastTransactionStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MandateCreationDate"]) -> typing.Union[MetaOapg.properties.MandateCreationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MandateID"]) -> typing.Union[MetaOapg.properties.MandateID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MandateReceived"]) -> typing.Union[MetaOapg.properties.MandateReceived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MandateUpdateDate"]) -> typing.Union[MetaOapg.properties.MandateUpdateDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MaxConsecutivePaymentFailures"]) -> typing.Union[MetaOapg.properties.MaxConsecutivePaymentFailures, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NumConsecutiveFailures"]) -> typing.Union[MetaOapg.properties.NumConsecutiveFailures, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaymentMethodId"]) -> typing.Union[MetaOapg.properties.PaymentMethodId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaymentMethodStatus"]) -> typing.Union[MetaOapg.properties.PaymentMethodStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaymentRetryWindow"]) -> typing.Union[MetaOapg.properties.PaymentRetryWindow, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaypalBaid"]) -> typing.Union[MetaOapg.properties.PaypalBaid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaypalEmail"]) -> typing.Union[MetaOapg.properties.PaypalEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaypalPreapprovalKey"]) -> typing.Union[MetaOapg.properties.PaypalPreapprovalKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaypalType"]) -> typing.Union[MetaOapg.properties.PaypalType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Phone"]) -> typing.Union[MetaOapg.properties.Phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PostalCode"]) -> typing.Union[MetaOapg.properties.PostalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SecondTokenId"]) -> typing.Union[MetaOapg.properties.SecondTokenId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["State"]) -> typing.Union[MetaOapg.properties.State, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StreetName"]) -> typing.Union[MetaOapg.properties.StreetName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StreetNumber"]) -> typing.Union[MetaOapg.properties.StreetNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TokenId"]) -> typing.Union[MetaOapg.properties.TokenId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalNumberOfErrorPayments"]) -> typing.Union[MetaOapg.properties.TotalNumberOfErrorPayments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalNumberOfProcessedPayments"]) -> typing.Union[MetaOapg.properties.TotalNumberOfProcessedPayments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> typing.Union[MetaOapg.properties.Type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UseDefaultRetryRule"]) -> typing.Union[MetaOapg.properties.UseDefaultRetryRule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "AchAbaCode", "AchAccountName", "AchAccountNumberMask", "AchAccountType", "AchBankName", "BankBranchCode", "BankCheckDigit", "BankCity", "BankCode", "BankIdentificationNumber", "BankName", "BankPostalCode", "BankStreetName", "BankStreetNumber", "BankTransferAccountName", "BankTransferAccountNumberMask", "BankTransferAccountType", "BankTransferType", "BusinessIdentificationCode", "City", "CompanyName", "Country", "CreditCardAddress1", "CreditCardAddress2", "CreditCardCity", "CreditCardCountry", "CreditCardExpirationMonth", "CreditCardExpirationYear", "CreditCardHolderName", "CreditCardMaskNumber", "CreditCardPostalCode", "CreditCardState", "CreditCardType", "DeviceSessionId", "Email", "ExistingMandate", "FirstName", "IBAN", "IPAddress", "Id", "IdentityNumber", "IsCompany", "LastFailedSaleTransactionDate", "LastName", "LastTransactionDateTime", "LastTransactionStatus", "MandateCreationDate", "MandateID", "MandateReceived", "MandateUpdateDate", "MaxConsecutivePaymentFailures", "Name", "NumConsecutiveFailures", "PaymentMethodId", "PaymentMethodStatus", "PaymentRetryWindow", "PaypalBaid", "PaypalEmail", "PaypalPreapprovalKey", "PaypalType", "Phone", "PostalCode", "SecondTokenId", "State", "StreetName", "StreetNumber", "TokenId", "TotalNumberOfErrorPayments", "TotalNumberOfProcessedPayments", "Type", "UseDefaultRetryRule", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AccountId: typing.Union[MetaOapg.properties.AccountId, str, schemas.Unset] = schemas.unset,
        AchAbaCode: typing.Union[MetaOapg.properties.AchAbaCode, str, schemas.Unset] = schemas.unset,
        AchAccountName: typing.Union[MetaOapg.properties.AchAccountName, str, schemas.Unset] = schemas.unset,
        AchAccountNumberMask: typing.Union[MetaOapg.properties.AchAccountNumberMask, str, schemas.Unset] = schemas.unset,
        AchAccountType: typing.Union[MetaOapg.properties.AchAccountType, str, schemas.Unset] = schemas.unset,
        AchBankName: typing.Union[MetaOapg.properties.AchBankName, str, schemas.Unset] = schemas.unset,
        BankBranchCode: typing.Union[MetaOapg.properties.BankBranchCode, str, schemas.Unset] = schemas.unset,
        BankCheckDigit: typing.Union[MetaOapg.properties.BankCheckDigit, str, schemas.Unset] = schemas.unset,
        BankCity: typing.Union[MetaOapg.properties.BankCity, str, schemas.Unset] = schemas.unset,
        BankCode: typing.Union[MetaOapg.properties.BankCode, str, schemas.Unset] = schemas.unset,
        BankIdentificationNumber: typing.Union[MetaOapg.properties.BankIdentificationNumber, str, schemas.Unset] = schemas.unset,
        BankName: typing.Union[MetaOapg.properties.BankName, str, schemas.Unset] = schemas.unset,
        BankPostalCode: typing.Union[MetaOapg.properties.BankPostalCode, str, schemas.Unset] = schemas.unset,
        BankStreetName: typing.Union[MetaOapg.properties.BankStreetName, str, schemas.Unset] = schemas.unset,
        BankStreetNumber: typing.Union[MetaOapg.properties.BankStreetNumber, str, schemas.Unset] = schemas.unset,
        BankTransferAccountName: typing.Union[MetaOapg.properties.BankTransferAccountName, str, schemas.Unset] = schemas.unset,
        BankTransferAccountNumberMask: typing.Union[MetaOapg.properties.BankTransferAccountNumberMask, str, schemas.Unset] = schemas.unset,
        BankTransferAccountType: typing.Union[MetaOapg.properties.BankTransferAccountType, str, schemas.Unset] = schemas.unset,
        BankTransferType: typing.Union[MetaOapg.properties.BankTransferType, str, schemas.Unset] = schemas.unset,
        BusinessIdentificationCode: typing.Union[MetaOapg.properties.BusinessIdentificationCode, str, schemas.Unset] = schemas.unset,
        City: typing.Union[MetaOapg.properties.City, str, schemas.Unset] = schemas.unset,
        CompanyName: typing.Union[MetaOapg.properties.CompanyName, str, schemas.Unset] = schemas.unset,
        Country: typing.Union[MetaOapg.properties.Country, str, schemas.Unset] = schemas.unset,
        CreditCardAddress1: typing.Union[MetaOapg.properties.CreditCardAddress1, str, schemas.Unset] = schemas.unset,
        CreditCardAddress2: typing.Union[MetaOapg.properties.CreditCardAddress2, str, schemas.Unset] = schemas.unset,
        CreditCardCity: typing.Union[MetaOapg.properties.CreditCardCity, str, schemas.Unset] = schemas.unset,
        CreditCardCountry: typing.Union[MetaOapg.properties.CreditCardCountry, str, schemas.Unset] = schemas.unset,
        CreditCardExpirationMonth: typing.Union[MetaOapg.properties.CreditCardExpirationMonth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        CreditCardExpirationYear: typing.Union[MetaOapg.properties.CreditCardExpirationYear, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        CreditCardHolderName: typing.Union[MetaOapg.properties.CreditCardHolderName, str, schemas.Unset] = schemas.unset,
        CreditCardMaskNumber: typing.Union[MetaOapg.properties.CreditCardMaskNumber, str, schemas.Unset] = schemas.unset,
        CreditCardPostalCode: typing.Union[MetaOapg.properties.CreditCardPostalCode, str, schemas.Unset] = schemas.unset,
        CreditCardState: typing.Union[MetaOapg.properties.CreditCardState, str, schemas.Unset] = schemas.unset,
        CreditCardType: typing.Union[MetaOapg.properties.CreditCardType, str, schemas.Unset] = schemas.unset,
        DeviceSessionId: typing.Union[MetaOapg.properties.DeviceSessionId, str, schemas.Unset] = schemas.unset,
        Email: typing.Union[MetaOapg.properties.Email, str, schemas.Unset] = schemas.unset,
        ExistingMandate: typing.Union[MetaOapg.properties.ExistingMandate, str, schemas.Unset] = schemas.unset,
        FirstName: typing.Union[MetaOapg.properties.FirstName, str, schemas.Unset] = schemas.unset,
        IBAN: typing.Union[MetaOapg.properties.IBAN, str, schemas.Unset] = schemas.unset,
        IPAddress: typing.Union[MetaOapg.properties.IPAddress, str, schemas.Unset] = schemas.unset,
        Id: typing.Union[MetaOapg.properties.Id, str, schemas.Unset] = schemas.unset,
        IdentityNumber: typing.Union[MetaOapg.properties.IdentityNumber, str, schemas.Unset] = schemas.unset,
        IsCompany: typing.Union[MetaOapg.properties.IsCompany, bool, schemas.Unset] = schemas.unset,
        LastFailedSaleTransactionDate: typing.Union[MetaOapg.properties.LastFailedSaleTransactionDate, str, datetime, schemas.Unset] = schemas.unset,
        LastName: typing.Union[MetaOapg.properties.LastName, str, schemas.Unset] = schemas.unset,
        LastTransactionDateTime: typing.Union[MetaOapg.properties.LastTransactionDateTime, str, datetime, schemas.Unset] = schemas.unset,
        LastTransactionStatus: typing.Union[MetaOapg.properties.LastTransactionStatus, str, schemas.Unset] = schemas.unset,
        MandateCreationDate: typing.Union[MetaOapg.properties.MandateCreationDate, str, date, schemas.Unset] = schemas.unset,
        MandateID: typing.Union[MetaOapg.properties.MandateID, str, schemas.Unset] = schemas.unset,
        MandateReceived: typing.Union[MetaOapg.properties.MandateReceived, str, schemas.Unset] = schemas.unset,
        MandateUpdateDate: typing.Union[MetaOapg.properties.MandateUpdateDate, str, date, schemas.Unset] = schemas.unset,
        MaxConsecutivePaymentFailures: typing.Union[MetaOapg.properties.MaxConsecutivePaymentFailures, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
        NumConsecutiveFailures: typing.Union[MetaOapg.properties.NumConsecutiveFailures, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        PaymentMethodId: typing.Union[MetaOapg.properties.PaymentMethodId, str, schemas.Unset] = schemas.unset,
        PaymentMethodStatus: typing.Union[MetaOapg.properties.PaymentMethodStatus, str, schemas.Unset] = schemas.unset,
        PaymentRetryWindow: typing.Union[MetaOapg.properties.PaymentRetryWindow, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        PaypalBaid: typing.Union[MetaOapg.properties.PaypalBaid, str, schemas.Unset] = schemas.unset,
        PaypalEmail: typing.Union[MetaOapg.properties.PaypalEmail, str, schemas.Unset] = schemas.unset,
        PaypalPreapprovalKey: typing.Union[MetaOapg.properties.PaypalPreapprovalKey, str, schemas.Unset] = schemas.unset,
        PaypalType: typing.Union[MetaOapg.properties.PaypalType, str, schemas.Unset] = schemas.unset,
        Phone: typing.Union[MetaOapg.properties.Phone, str, schemas.Unset] = schemas.unset,
        PostalCode: typing.Union[MetaOapg.properties.PostalCode, str, schemas.Unset] = schemas.unset,
        SecondTokenId: typing.Union[MetaOapg.properties.SecondTokenId, str, schemas.Unset] = schemas.unset,
        State: typing.Union[MetaOapg.properties.State, str, schemas.Unset] = schemas.unset,
        StreetName: typing.Union[MetaOapg.properties.StreetName, str, schemas.Unset] = schemas.unset,
        StreetNumber: typing.Union[MetaOapg.properties.StreetNumber, str, schemas.Unset] = schemas.unset,
        TokenId: typing.Union[MetaOapg.properties.TokenId, str, schemas.Unset] = schemas.unset,
        TotalNumberOfErrorPayments: typing.Union[MetaOapg.properties.TotalNumberOfErrorPayments, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TotalNumberOfProcessedPayments: typing.Union[MetaOapg.properties.TotalNumberOfProcessedPayments, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Type: typing.Union[MetaOapg.properties.Type, str, schemas.Unset] = schemas.unset,
        UseDefaultRetryRule: typing.Union[MetaOapg.properties.UseDefaultRetryRule, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProxyGetPaymentMethodSnapshot':
        return super().__new__(
            cls,
            *args,
            AccountId=AccountId,
            AchAbaCode=AchAbaCode,
            AchAccountName=AchAccountName,
            AchAccountNumberMask=AchAccountNumberMask,
            AchAccountType=AchAccountType,
            AchBankName=AchBankName,
            BankBranchCode=BankBranchCode,
            BankCheckDigit=BankCheckDigit,
            BankCity=BankCity,
            BankCode=BankCode,
            BankIdentificationNumber=BankIdentificationNumber,
            BankName=BankName,
            BankPostalCode=BankPostalCode,
            BankStreetName=BankStreetName,
            BankStreetNumber=BankStreetNumber,
            BankTransferAccountName=BankTransferAccountName,
            BankTransferAccountNumberMask=BankTransferAccountNumberMask,
            BankTransferAccountType=BankTransferAccountType,
            BankTransferType=BankTransferType,
            BusinessIdentificationCode=BusinessIdentificationCode,
            City=City,
            CompanyName=CompanyName,
            Country=Country,
            CreditCardAddress1=CreditCardAddress1,
            CreditCardAddress2=CreditCardAddress2,
            CreditCardCity=CreditCardCity,
            CreditCardCountry=CreditCardCountry,
            CreditCardExpirationMonth=CreditCardExpirationMonth,
            CreditCardExpirationYear=CreditCardExpirationYear,
            CreditCardHolderName=CreditCardHolderName,
            CreditCardMaskNumber=CreditCardMaskNumber,
            CreditCardPostalCode=CreditCardPostalCode,
            CreditCardState=CreditCardState,
            CreditCardType=CreditCardType,
            DeviceSessionId=DeviceSessionId,
            Email=Email,
            ExistingMandate=ExistingMandate,
            FirstName=FirstName,
            IBAN=IBAN,
            IPAddress=IPAddress,
            Id=Id,
            IdentityNumber=IdentityNumber,
            IsCompany=IsCompany,
            LastFailedSaleTransactionDate=LastFailedSaleTransactionDate,
            LastName=LastName,
            LastTransactionDateTime=LastTransactionDateTime,
            LastTransactionStatus=LastTransactionStatus,
            MandateCreationDate=MandateCreationDate,
            MandateID=MandateID,
            MandateReceived=MandateReceived,
            MandateUpdateDate=MandateUpdateDate,
            MaxConsecutivePaymentFailures=MaxConsecutivePaymentFailures,
            Name=Name,
            NumConsecutiveFailures=NumConsecutiveFailures,
            PaymentMethodId=PaymentMethodId,
            PaymentMethodStatus=PaymentMethodStatus,
            PaymentRetryWindow=PaymentRetryWindow,
            PaypalBaid=PaypalBaid,
            PaypalEmail=PaypalEmail,
            PaypalPreapprovalKey=PaypalPreapprovalKey,
            PaypalType=PaypalType,
            Phone=Phone,
            PostalCode=PostalCode,
            SecondTokenId=SecondTokenId,
            State=State,
            StreetName=StreetName,
            StreetNumber=StreetNumber,
            TokenId=TokenId,
            TotalNumberOfErrorPayments=TotalNumberOfErrorPayments,
            TotalNumberOfProcessedPayments=TotalNumberOfProcessedPayments,
            Type=Type,
            UseDefaultRetryRule=UseDefaultRetryRule,
            _configuration=_configuration,
            **kwargs,
        )

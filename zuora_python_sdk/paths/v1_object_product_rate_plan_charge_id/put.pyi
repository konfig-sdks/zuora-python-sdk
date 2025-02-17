# coding: utf-8

"""
    API Reference

      # Introduction  Welcome to the REST API reference for the Zuora Billing, Payments, and Central Platform!  To learn about the common use cases of Zuora REST APIs, check out the [REST API Tutorials](https://developer.zuora.com/rest-api/api-guides/overview/).  In addition to Zuora API Reference, we also provide API references for other Zuora products:    * [Revenue API Reference](https://developer.zuora.com/api-references/revenue/overview/)   * [Collections API Reference](https://developer.zuora.com/api-references/collections/overview/)        The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Billing Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  Some of our older APIs are no longer recommended but still available, not affecting any existing integration. To find related API documentation, see [Older API Reference](https://developer.zuora.com/api-references/older-api/overview/).   ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Cloud 1 Production | https://rest.na.zuora.com  | |US Cloud 1 API Sandbox |  https://rest.sandbox.na.zuora.com | |US Cloud 2 Production | https://rest.zuora.com | |US Cloud 2 API Sandbox | https://rest.apisandbox.zuora.com| |US Central Sandbox | https://rest.test.zuora.com |   |US Performance Test | https://rest.pt1.zuora.com | |US Production Copy | Submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints. See [REST endpoint base URL of Production Copy (Service) Environment for existing and new customers](https://community.zuora.com/t5/API/REST-endpoint-base-URL-of-Production-Copy-Service-Environment/td-p/29611) for more information. | |EU Production | https://rest.eu.zuora.com | |EU API Sandbox | https://rest.sandbox.eu.zuora.com | |EU Central Sandbox | https://rest.test.eu.zuora.com |  The Production endpoint provides access to your live user data. Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision a Sandbox tenant for you, contact your Zuora representative for assistance.   If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.   # Error Handling  If a request to Zuora Billing REST API with an endpoint starting with `/v1` (except [Actions](https://developer.zuora.com/api-references/api/tag/Actions) and CRUD operations) fails, the response will contain an eight-digit error code with a corresponding error message to indicate the details of the error.  The following code snippet is a sample error response that contains an error code and message pair:  ```  {    \"success\": false,    \"processId\": \"CBCFED6580B4E076\",    \"reasons\":  [      {       \"code\": 53100320,       \"message\": \"'termType' value should be one of: TERMED, EVERGREEN\"      }     ]  } ``` The `success` field indicates whether the API request has succeeded. The `processId` field is a Zuora internal ID that you can provide to Zuora Global Support for troubleshooting purposes.  The `reasons` field contains the actual error code and message pair. The error code begins with `5` or `6` means that you encountered a certain issue that is specific to a REST API resource in Zuora Billing, Payments, and Central Platform. For example, `53100320` indicates that an invalid value is specified for the `termType` field of the `subscription` object.  The error code beginning with `9` usually indicates that an authentication-related issue occurred, and it can also indicate other unexpected errors depending on different cases. For example, `90000011` indicates that an invalid credential is provided in the request header.   When troubleshooting the error, you can divide the error code into two components: REST API resource code and error category code. See the following Zuora error code sample:  <a href=\"https://developer.zuora.com/images/ZuoraErrorCode.jpeg\" target=\"_blank\"><img src=\"https://developer.zuora.com/images/ZuoraErrorCode.jpeg\" alt=\"Zuora Error Code Sample\"></a>   **Note:** Zuora determines resource codes based on the request payload. Therefore, if GET and DELETE requests that do not contain payloads fail, you will get `500000` as the resource code, which indicates an unknown object and an unknown field.  The error category code of these requests is valid and follows the rules described in the [Error Category Codes](https://developer.zuora.com/api-references/api/overview/#section/Error-Handling/Error-Category-Codes) section.  In such case, you can refer to the returned error message to troubleshoot.   ## REST API Resource Codes  The 6-digit resource code indicates the REST API resource, typically a field of a Zuora object, on which the issue occurs. In the preceding example, `531003` refers to the `termType` field of the `subscription` object.   The value range for all REST API resource codes is from `500000` to `679999`. See <a href=\"https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Resource_Codes\" target=\"_blank\">Resource Codes</a> in the Knowledge Center for a full list of resource codes.  ## Error Category Codes  The 2-digit error category code identifies the type of error, for example, resource not found or missing required field.   The following table describes all error categories and the corresponding resolution:  | Code    | Error category              | Description    | Resolution    | |:--------|:--------|:--------|:--------| | 10      | Permission or access denied | The request cannot be processed because a certain tenant or user permission is missing. | Check the missing tenant or user permission in the response message and contact <a href=\"https://support.zuora.com\" target=\"_blank\">Zuora Global Support</a> for enablement. | | 11      | Authentication failed       | Authentication fails due to invalid API authentication credentials. | Ensure that a valid API credential is specified. | | 20      | Invalid format or value     | The request cannot be processed due to an invalid field format or value. | Check the invalid field in the error message, and ensure that the format and value of all fields you passed in are valid. | | 21      | Unknown field in request    | The request cannot be processed because an unknown field exists in the request body. | Check the unknown field name in the response message, and ensure that you do not include any unknown field in the request body. | | 22      | Missing required field      | The request cannot be processed because a required field in the request body is missing. | Check the missing field name in the response message, and ensure that you include all required fields in the request body. | | 23      | Missing required parameter  | The request cannot be processed because a required query parameter is missing. | Check the missing parameter name in the response message, and ensure that you include the parameter in the query. | | 30      | Rule restriction            | The request cannot be processed due to the violation of a Zuora business rule. | Check the response message and ensure that the API request meets the specified business rules. | | 40      | Not found                   | The specified resource cannot be found. | Check the response message and ensure that the specified resource exists in your Zuora tenant. | | 45      | Unsupported request         | The requested endpoint does not support the specified HTTP method. | Check your request and ensure that the endpoint and method matches. | | 50      | Locking contention          | This request cannot be processed because the objects this request is trying to modify are being modified by another API request, UI operation, or batch job process. | <p>Resubmit the request first to have another try.</p> <p>If this error still occurs, contact <a href=\"https://support.zuora.com\" target=\"_blank\">Zuora Global Support</a> with the returned `Zuora-Request-Id` value in the response header for assistance.</p> | | 60      | Internal error              | The server encounters an internal error. | Contact <a href=\"https://support.zuora.com\" target=\"_blank\">Zuora Global Support</a> with the returned `Zuora-Request-Id` value in the response header for assistance. | | 61      | Temporary error             | A temporary error occurs during request processing, for example, a database communication error. | <p>Resubmit the request first to have another try.</p> <p>If this error still occurs, contact <a href=\"https://support.zuora.com\" target=\"_blank\">Zuora Global Support</a> with the returned `Zuora-Request-Id` value in the response header for assistance. </p>| | 70      | Request exceeded limit      | The total number of concurrent requests exceeds the limit allowed by the system. | <p>Resubmit the request after the number of seconds specified by the `Retry-After` value in the response header.</p> <p>Check [Concurrent request limits](https://developer.zuora.com/rest-api/general-concepts/rate-concurrency-limits/) for details about Zuora’s concurrent request limit policy.</p> | | 90      | Malformed request           | The request cannot be processed due to JSON syntax errors. | Check the syntax error in the JSON request body and ensure that the request is in the correct JSON format. | | 99      | Integration error           | The server encounters an error when communicating with an external system, for example, payment gateway, tax engine provider. | Check the response message and take action accordingly. |   # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.   ## Major Version   The major version number of the REST API appears in the REST URL. In this API reference, only the **v1** major version is available. For example, `POST https://rest.zuora.com/v1/subscriptions`.       Zuora also offers the [Quickstart API](https://developer.zuora.com/quickstart-api/quickstart-api-introduction/) that uses the **v2** major version. For more information about which version to use, see [Which API Should I Use](https://developer.zuora.com/api-reference-guide/).   ## Minor Version   Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.    Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not consecutive.  You can use the following versions to override the default version (`186.0`):   - 187.0   - 188.0   - 189.0   - 196.0   - 206.0   - 207.0   - 211.0   - 214.0   - 215.0   - 216.0   - 223.0   - 224.0   - 230.0   - 239.0   - 256.0   - 257.0   - 309.0   - 314.0   - 315.0   - 329.0   - 330.0   - 336.0   - 337.0   - 338.0   - 341.0  If you set the `zuora-version` header to a version excluded from the preceding list, the corresponding API request is processed as you use the default version, `186.0`.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 206.0 and earlier  | [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 206.0 and earlier| [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 206.0 and earlier| [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://developer.zuora.com/api-references/api/operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://developer.zuora.com/api-references/api/operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://developer.zuora.com/api-references/api/operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://developer.zuora.com/api-references/api/operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://developer.zuora.com/api-references/api/operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://developer.zuora.com/api-references/api/operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://developer.zuora.com/api-references/api/operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://developer.zuora.com/api-references/api/operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://developer.zuora.com/api-references/api/operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://developer.zuora.com/api-references/api/operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://developer.zuora.com/api-references/api/operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://developer.zuora.com/api-references/api/operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. | | chargeId | 256.0 and earlier | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | productRatePlanChargeId | 257.0 and later | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | comment | 256.0 and earlier | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItem \"Get debit memo item\") | Comments about the product rate plan charge, invoice item, or memo item. | | description | 257.0 and later | [Create credit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://developer.zuora.com/api-references/api/operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://developer.zuora.com/api-references/api/operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://developer.zuora.com/api-references/api/operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://developer.zuora.com/api-references/api/operation/GET_DebitMemoItem \"Get debit memo item\") | Description of the the product rate plan charge, invoice item, or memo item. | | taxationItems | 309.0 and later | [Preview an order](https://developer.zuora.com/api-references/api/operation/POST_PreviewOrder \"Preview an order\") | List of taxation items for an invoice item or a credit memo item. | | batch | 309.0 and earlier | [Create a billing preview run](https://developer.zuora.com/api-references/api/operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. |       | batches | 314.0 and later | [Create a billing preview run](https://developer.zuora.com/api-references/api/operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. | | taxationItems | 315.0 and later | [Preview a subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription \"Preview a subscription\"); [Update a subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update a subscription\")| List of taxation items for an invoice item or a credit memo item. | | billingDocument | 330.0 and later | [Create a payment schedule](https://developer.zuora.com/api-references/api/operation/POST_PaymentSchedule \"Create a payment schedule\"); [Create multiple payment schedules at once](https://developer.zuora.com/api-references/api/operation/POST_PaymentSchedules \"Create multiple payment schedules at once\")| The billing document with which the payment schedule item is associated. | | paymentId | 336.0 and earlier | [Add payment schedule items to a custom payment schedule](https://developer.zuora.com/api-references/api/operation/POST_AddItemsToCustomPaymentSchedule/ \"Add payment schedule items to a custom payment schedule\"); [Update a payment schedule](https://developer.zuora.com/api-references/api/operation/PUT_PaymentSchedule/ \"Update a payment schedule\"); [Update a payment schedule item](https://developer.zuora.com/api-references/api/operation/PUT_PaymentScheduleItem/ \"Update a payment schedule item\"); [Preview the result of payment schedule update](https://developer.zuora.com/api-references/api/operation/PUT_PaymentScheduleUpdatePreview/ \"Preview the result of payment schedule update\"); [Retrieve a payment schedule](https://developer.zuora.com/api-references/api/operation/GET_PaymentSchedule/ \"Retrieve a payment schedule\"); [Retrieve a payment schedule item](https://developer.zuora.com/api-references/api/operation/GET_PaymentScheduleItem/ \"Retrieve a payment schedule item\"); [List payment schedules by customer account](https://developer.zuora.com/api-references/api/operation/GET_PaymentSchedules/ \"List payment schedules by customer account\"); [Cancel a payment schedule](https://developer.zuora.com/api-references/api/operation/PUT_CancelPaymentSchedule/ \"Cancel a payment schedule\"); [Cancel a payment schedule item](https://developer.zuora.com/api-references/api/operation/PUT_CancelPaymentScheduleItem/ \"Cancel a payment schedule item\");[Skip a payment schedule item](https://developer.zuora.com/api-references/api/operation/PUT_SkipPaymentScheduleItem/ \"Skip a payment schedule item\");[Retry failed payment schedule items](https://developer.zuora.com/api-references/api/operation/POST_RetryPaymentScheduleItem/ \"Retry failed payment schedule items\") | ID of the payment to be linked to the payment schedule item.   #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://developer.zuora.com/api-references/api/operation/POST_PreviewSubscription) and [Update Subscription](https://developer.zuora.com/api-references/api/operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics   # API Names for Zuora Objects  For information about the Zuora business object model, see [Zuora Business Object Model](https://developer.zuora.com/rest-api/general-concepts/object-model/).  You can use the [Describe](https://developer.zuora.com/api-references/api/operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun` - API name used  in the [Describe](https://developer.zuora.com/api-references/api/operation/GET_Describe) operation, Export ZOQL queries, and Data Query.</p> <p>`BillRun` - API name used in the [Actions](https://developer.zuora.com/api-references/api/tag/Actions). See the CRUD oprations of [Bill Run](https://developer.zuora.com/api-references/api/tag/Bill-Run) for more information about the `BillRun` object. `BillingRun` and `BillRun` have different fields. |                      | Billing Preview Run                           | `BillingPreviewRun`                        |                      | Configuration Templates                       | `ConfigurationTemplates`                   | | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Fulfillment                                   | `Fulfillment`                              | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Invoice Schedule                              | `InvoiceSchedule`                          | | Invoice Schedule Item                         | `InvoiceScheduleItem`                      | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Notification History - Callout                | `CalloutHistory`                           | | Notification History - Email                  | `EmailHistory`                             | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Line Items                              | `OrderLineItems`                           |     | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                        | `UpdaterDetail`                             | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Charge Definition                     | `ProductChargeDefinition`                  |     | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Definition                  | `ProductRatePlanDefinition`                |     | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    | 

    The version of the OpenAPI document: 2024-03-15
    Contact: docs@zuora.com
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from zuora_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from zuora_python_sdk.api_response import AsyncGeneratorResponse
from zuora_python_sdk import api_client, exceptions
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

from zuora_python_sdk.model.proxy_modify_product_rate_plan_charge import ProxyModifyProductRatePlanCharge as ProxyModifyProductRatePlanChargeSchema
from zuora_python_sdk.model.proxy_no_data_response import ProxyNoDataResponse as ProxyNoDataResponseSchema
from zuora_python_sdk.model.proxy_create_or_modify_product_rate_plan_charge_tier_data import ProxyCreateOrModifyProductRatePlanChargeTierData as ProxyCreateOrModifyProductRatePlanChargeTierDataSchema
from zuora_python_sdk.model.proxy_unauthorized_response import ProxyUnauthorizedResponse as ProxyUnauthorizedResponseSchema
from zuora_python_sdk.model.proxy_create_or_modify_product_rate_plan_charge_charge_model_configuration import ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration as ProxyCreateOrModifyProductRatePlanChargeChargeModelConfigurationSchema
from zuora_python_sdk.model.proxy_create_or_modify_response import ProxyCreateOrModifyResponse as ProxyCreateOrModifyResponseSchema
from zuora_python_sdk.model.proxy_create_or_modify_delivery_schedule import ProxyCreateOrModifyDeliverySchedule as ProxyCreateOrModifyDeliveryScheduleSchema

from zuora_python_sdk.type.proxy_create_or_modify_product_rate_plan_charge_charge_model_configuration import ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration
from zuora_python_sdk.type.proxy_create_or_modify_delivery_schedule import ProxyCreateOrModifyDeliverySchedule
from zuora_python_sdk.type.proxy_no_data_response import ProxyNoDataResponse
from zuora_python_sdk.type.proxy_unauthorized_response import ProxyUnauthorizedResponse
from zuora_python_sdk.type.proxy_modify_product_rate_plan_charge import ProxyModifyProductRatePlanCharge
from zuora_python_sdk.type.proxy_create_or_modify_response import ProxyCreateOrModifyResponse
from zuora_python_sdk.type.proxy_create_or_modify_product_rate_plan_charge_tier_data import ProxyCreateOrModifyProductRatePlanChargeTierData

from ...api_client import Dictionary
from zuora_python_sdk.pydantic.proxy_no_data_response import ProxyNoDataResponse as ProxyNoDataResponsePydantic
from zuora_python_sdk.pydantic.proxy_modify_product_rate_plan_charge import ProxyModifyProductRatePlanCharge as ProxyModifyProductRatePlanChargePydantic
from zuora_python_sdk.pydantic.proxy_unauthorized_response import ProxyUnauthorizedResponse as ProxyUnauthorizedResponsePydantic
from zuora_python_sdk.pydantic.proxy_create_or_modify_response import ProxyCreateOrModifyResponse as ProxyCreateOrModifyResponsePydantic
from zuora_python_sdk.pydantic.proxy_create_or_modify_product_rate_plan_charge_charge_model_configuration import ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration as ProxyCreateOrModifyProductRatePlanChargeChargeModelConfigurationPydantic
from zuora_python_sdk.pydantic.proxy_create_or_modify_delivery_schedule import ProxyCreateOrModifyDeliverySchedule as ProxyCreateOrModifyDeliverySchedulePydantic
from zuora_python_sdk.pydantic.proxy_create_or_modify_product_rate_plan_charge_tier_data import ProxyCreateOrModifyProductRatePlanChargeTierData as ProxyCreateOrModifyProductRatePlanChargeTierDataPydantic

# Query params
RejectUnknownFieldsSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'rejectUnknownFields': typing.Union[RejectUnknownFieldsSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_reject_unknown_fields = api_client.QueryParameter(
    name="rejectUnknownFields",
    style=api_client.ParameterStyle.FORM,
    schema=RejectUnknownFieldsSchema,
    explode=True,
)
# Header params
AcceptEncodingSchema = schemas.StrSchema
ContentEncodingSchema = schemas.StrSchema
AuthorizationSchema = schemas.StrSchema
ZuoraEntityIdsSchema = schemas.StrSchema
ZuoraOrgIdsSchema = schemas.StrSchema


class ZuoraTrackIdSchema(
    schemas.StrSchema
):
    pass
XZuoraWSDLVersionSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'Accept-Encoding': typing.Union[AcceptEncodingSchema, str, ],
        'Content-Encoding': typing.Union[ContentEncodingSchema, str, ],
        'Authorization': typing.Union[AuthorizationSchema, str, ],
        'Zuora-Entity-Ids': typing.Union[ZuoraEntityIdsSchema, str, ],
        'Zuora-Org-Ids': typing.Union[ZuoraOrgIdsSchema, str, ],
        'Zuora-Track-Id': typing.Union[ZuoraTrackIdSchema, str, ],
        'X-Zuora-WSDL-Version': typing.Union[XZuoraWSDLVersionSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_accept_encoding = api_client.HeaderParameter(
    name="Accept-Encoding",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AcceptEncodingSchema,
)
request_header_content_encoding = api_client.HeaderParameter(
    name="Content-Encoding",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentEncodingSchema,
)
request_header_authorization = api_client.HeaderParameter(
    name="Authorization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthorizationSchema,
)
request_header_zuora_entity_ids = api_client.HeaderParameter(
    name="Zuora-Entity-Ids",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ZuoraEntityIdsSchema,
)
request_header_zuora_org_ids = api_client.HeaderParameter(
    name="Zuora-Org-Ids",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ZuoraOrgIdsSchema,
)
request_header_zuora_track_id = api_client.HeaderParameter(
    name="Zuora-Track-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ZuoraTrackIdSchema,
)
request_header_x_zuora_wsdl_version = api_client.HeaderParameter(
    name="X-Zuora-WSDL-Version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XZuoraWSDLVersionSchema,
)
# Path params
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ProxyModifyProductRatePlanChargeSchema


request_body_proxy_modify_product_rate_plan_charge = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
ContentEncodingSchema = schemas.StrSchema
RateLimitLimitSchema = schemas.StrSchema
RateLimitRemainingSchema = schemas.NumberSchema
RateLimitResetSchema = schemas.NumberSchema


class ZuoraRequestIdSchema(
    schemas.StrSchema
):
    pass


class ZuoraTrackIdSchema(
    schemas.StrSchema
):
    pass
SchemaFor200ResponseBodyApplicationJson = ProxyCreateOrModifyResponseSchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'Content-Encoding': ContentEncodingSchema,
        'RateLimit-Limit': RateLimitLimitSchema,
        'RateLimit-Remaining': RateLimitRemainingSchema,
        'RateLimit-Reset': RateLimitResetSchema,
        'Zuora-Request-Id': ZuoraRequestIdSchema,
        'Zuora-Track-Id': ZuoraTrackIdSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ProxyCreateOrModifyResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ProxyCreateOrModifyResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
    headers=[
        content_encoding_parameter,
        rate_limit_limit_parameter,
        rate_limit_remaining_parameter,
        rate_limit_reset_parameter,
        zuora_request_id_parameter,
        zuora_track_id_parameter,
    ]
)
ContentEncodingSchema = schemas.StrSchema
RateLimitLimitSchema = schemas.StrSchema
RateLimitRemainingSchema = schemas.NumberSchema
RateLimitResetSchema = schemas.NumberSchema


class WWWAuthenticateSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def BASIC_REALMZUORA_API_ZSESSION_REALMZUORA_API_BEARER_REALMZUORA_API(cls):
        return cls("Basic realm=Zuora API, ZSession realm=Zuora API, Bearer realm=Zuora API")


class ZuoraRequestIdSchema(
    schemas.StrSchema
):
    pass


class ZuoraTrackIdSchema(
    schemas.StrSchema
):
    pass
SchemaFor401ResponseBodyApplicationJson = ProxyUnauthorizedResponseSchema
ResponseHeadersFor401 = typing_extensions.TypedDict(
    'ResponseHeadersFor401',
    {
        'Content-Encoding': ContentEncodingSchema,
        'RateLimit-Limit': RateLimitLimitSchema,
        'RateLimit-Remaining': RateLimitRemainingSchema,
        'RateLimit-Reset': RateLimitResetSchema,
        'WWW-Authenticate': WWWAuthenticateSchema,
        'Zuora-Request-Id': ZuoraRequestIdSchema,
        'Zuora-Track-Id': ZuoraTrackIdSchema,
    }
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ProxyUnauthorizedResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ProxyUnauthorizedResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
    headers=[
        content_encoding_parameter,
        rate_limit_limit_parameter,
        rate_limit_remaining_parameter,
        rate_limit_reset_parameter,
        www_authenticate_parameter,
        zuora_request_id_parameter,
        zuora_track_id_parameter,
    ]
)
ContentEncodingSchema = schemas.StrSchema
RateLimitLimitSchema = schemas.StrSchema
RateLimitRemainingSchema = schemas.NumberSchema
RateLimitResetSchema = schemas.NumberSchema


class ZuoraRequestIdSchema(
    schemas.StrSchema
):
    pass


class ZuoraTrackIdSchema(
    schemas.StrSchema
):
    pass
SchemaFor404ResponseBodyApplicationJson = ProxyNoDataResponseSchema
ResponseHeadersFor404 = typing_extensions.TypedDict(
    'ResponseHeadersFor404',
    {
        'Content-Encoding': ContentEncodingSchema,
        'RateLimit-Limit': RateLimitLimitSchema,
        'RateLimit-Remaining': RateLimitRemainingSchema,
        'RateLimit-Reset': RateLimitResetSchema,
        'Zuora-Request-Id': ZuoraRequestIdSchema,
        'Zuora-Track-Id': ZuoraTrackIdSchema,
    }
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ProxyNoDataResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ProxyNoDataResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
    headers=[
        content_encoding_parameter,
        rate_limit_limit_parameter,
        rate_limit_remaining_parameter,
        rate_limit_reset_parameter,
        zuora_request_id_parameter,
        zuora_track_id_parameter,
    ]
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _p_ut_product_rate_plan_charge_mapped_args(
        self,
        body: ProxyModifyProductRatePlanCharge,
        id: str,
        accounting_code: typing.Optional[str] = None,
        apply_discount_to: typing.Optional[str] = None,
        bill_cycle_day: typing.Optional[int] = None,
        bill_cycle_type: typing.Optional[str] = None,
        billing_period: typing.Optional[str] = None,
        billing_period_alignment: typing.Optional[str] = None,
        billing_timing: typing.Optional[str] = None,
        charge_function: typing.Optional[str] = None,
        commitment_type: typing.Optional[str] = None,
        charge_model: typing.Optional[str] = None,
        charge_model_configuration: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration] = None,
        credit_option: typing.Optional[str] = None,
        default_quantity: typing.Optional[typing.Union[int, float]] = None,
        deferred_revenue_account: typing.Optional[str] = None,
        delivery_schedule: typing.Optional[ProxyCreateOrModifyDeliverySchedule] = None,
        description: typing.Optional[str] = None,
        discount_level: typing.Optional[str] = None,
        drawdown_rate: typing.Optional[typing.Union[int, float]] = None,
        drawdown_uom: typing.Optional[str] = None,
        end_date_condition: typing.Optional[str] = None,
        exclude_item_billing_from_revenue_accounting: typing.Optional[bool] = None,
        exclude_item_booking_from_revenue_accounting: typing.Optional[bool] = None,
        included_units: typing.Optional[typing.Union[int, float]] = None,
        is_allocation_eligible: typing.Optional[bool] = None,
        is_prepaid: typing.Optional[bool] = None,
        is_rollover: typing.Optional[bool] = None,
        is_stacked_discount: typing.Optional[bool] = None,
        is_unbilled: typing.Optional[bool] = None,
        legacy_revenue_reporting: typing.Optional[bool] = None,
        list_price_base: typing.Optional[str] = None,
        max_quantity: typing.Optional[typing.Union[int, float]] = None,
        min_quantity: typing.Optional[typing.Union[int, float]] = None,
        name: typing.Optional[str] = None,
        number_of_period: typing.Optional[int] = None,
        overage_calculation_option: typing.Optional[typing.Optional[str]] = None,
        overage_unused_units_credit_option: typing.Optional[typing.Optional[str]] = None,
        prepaid_quantity: typing.Optional[typing.Union[int, float]] = None,
        prepaid_uom: typing.Optional[str] = None,
        price_change_option: typing.Optional[typing.Optional[str]] = None,
        price_increase_option: typing.Optional[str] = None,
        price_increase_percentage: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        product_category: typing.Optional[str] = None,
        product_class: typing.Optional[str] = None,
        product_family: typing.Optional[str] = None,
        product_line: typing.Optional[str] = None,
        revenue_recognition_timing: typing.Optional[str] = None,
        revenue_amortization_method: typing.Optional[str] = None,
        product_rate_plan_charge_number: typing.Optional[str] = None,
        product_rate_plan_charge_tier_data: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeTierData] = None,
        product_rate_plan_id: typing.Optional[str] = None,
        rating_group: typing.Optional[typing.Optional[str]] = None,
        recognized_revenue_account: typing.Optional[str] = None,
        rev_rec_code: typing.Optional[typing.Optional[str]] = None,
        rev_rec_trigger_condition: typing.Optional[typing.Optional[str]] = None,
        revenue_recognition_rule_name: typing.Optional[str] = None,
        rollover_apply: typing.Optional[str] = None,
        rollover_periods: typing.Optional[typing.Union[int, float]] = None,
        smoothing_model: typing.Optional[typing.Optional[str]] = None,
        specific_billing_period: typing.Optional[typing.Optional[int]] = None,
        specific_list_price_base: typing.Optional[typing.Optional[int]] = None,
        tax_code: typing.Optional[str] = None,
        tax_mode: typing.Optional[typing.Optional[str]] = None,
        taxable: typing.Optional[bool] = None,
        trigger_event: typing.Optional[str] = None,
        uom: typing.Optional[typing.Optional[str]] = None,
        up_to_periods: typing.Optional[typing.Optional[int]] = None,
        up_to_periods_type: typing.Optional[typing.Optional[str]] = None,
        usage_record_rating_option: typing.Optional[typing.Optional[str]] = None,
        use_discount_specific_accounting_code: typing.Optional[typing.Optional[bool]] = None,
        use_tenant_default_for_price_change: typing.Optional[bool] = None,
        validity_period_type: typing.Optional[str] = None,
        weekly_bill_cycle_day: typing.Optional[str] = None,
        apply_to_billing_period_partially: typing.Optional[bool] = None,
        rollover_period_length: typing.Optional[int] = None,
        formula: typing.Optional[str] = None,
        class__ns: typing.Optional[str] = None,
        deferred_rev_account__ns: typing.Optional[str] = None,
        department__ns: typing.Optional[str] = None,
        include_children__ns: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        item_type__ns: typing.Optional[str] = None,
        location__ns: typing.Optional[str] = None,
        recognized_rev_account__ns: typing.Optional[str] = None,
        rev_rec_end__ns: typing.Optional[str] = None,
        rev_rec_start__ns: typing.Optional[str] = None,
        rev_rec_template_type__ns: typing.Optional[str] = None,
        subsidiary__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        reject_unknown_fields: typing.Optional[bool] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        x_zuora_wsdl_version: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        _body = {}
        if accounting_code is not None:
            _body["AccountingCode"] = accounting_code
        if apply_discount_to is not None:
            _body["ApplyDiscountTo"] = apply_discount_to
        if bill_cycle_day is not None:
            _body["BillCycleDay"] = bill_cycle_day
        if bill_cycle_type is not None:
            _body["BillCycleType"] = bill_cycle_type
        if billing_period is not None:
            _body["BillingPeriod"] = billing_period
        if billing_period_alignment is not None:
            _body["BillingPeriodAlignment"] = billing_period_alignment
        if billing_timing is not None:
            _body["BillingTiming"] = billing_timing
        if charge_function is not None:
            _body["ChargeFunction"] = charge_function
        if commitment_type is not None:
            _body["CommitmentType"] = commitment_type
        if charge_model is not None:
            _body["ChargeModel"] = charge_model
        if charge_model_configuration is not None:
            _body["ChargeModelConfiguration"] = charge_model_configuration
        if credit_option is not None:
            _body["CreditOption"] = credit_option
        if default_quantity is not None:
            _body["DefaultQuantity"] = default_quantity
        if deferred_revenue_account is not None:
            _body["DeferredRevenueAccount"] = deferred_revenue_account
        if delivery_schedule is not None:
            _body["DeliverySchedule"] = delivery_schedule
        if description is not None:
            _body["Description"] = description
        if discount_level is not None:
            _body["DiscountLevel"] = discount_level
        if drawdown_rate is not None:
            _body["DrawdownRate"] = drawdown_rate
        if drawdown_uom is not None:
            _body["DrawdownUom"] = drawdown_uom
        if end_date_condition is not None:
            _body["EndDateCondition"] = end_date_condition
        if exclude_item_billing_from_revenue_accounting is not None:
            _body["ExcludeItemBillingFromRevenueAccounting"] = exclude_item_billing_from_revenue_accounting
        if exclude_item_booking_from_revenue_accounting is not None:
            _body["ExcludeItemBookingFromRevenueAccounting"] = exclude_item_booking_from_revenue_accounting
        if included_units is not None:
            _body["IncludedUnits"] = included_units
        if is_allocation_eligible is not None:
            _body["IsAllocationEligible"] = is_allocation_eligible
        if is_prepaid is not None:
            _body["IsPrepaid"] = is_prepaid
        if is_rollover is not None:
            _body["IsRollover"] = is_rollover
        if is_stacked_discount is not None:
            _body["IsStackedDiscount"] = is_stacked_discount
        if is_unbilled is not None:
            _body["IsUnbilled"] = is_unbilled
        if legacy_revenue_reporting is not None:
            _body["LegacyRevenueReporting"] = legacy_revenue_reporting
        if list_price_base is not None:
            _body["ListPriceBase"] = list_price_base
        if max_quantity is not None:
            _body["MaxQuantity"] = max_quantity
        if min_quantity is not None:
            _body["MinQuantity"] = min_quantity
        if name is not None:
            _body["Name"] = name
        if number_of_period is not None:
            _body["NumberOfPeriod"] = number_of_period
        if overage_calculation_option is not None:
            _body["OverageCalculationOption"] = overage_calculation_option
        if overage_unused_units_credit_option is not None:
            _body["OverageUnusedUnitsCreditOption"] = overage_unused_units_credit_option
        if prepaid_quantity is not None:
            _body["PrepaidQuantity"] = prepaid_quantity
        if prepaid_uom is not None:
            _body["PrepaidUom"] = prepaid_uom
        if price_change_option is not None:
            _body["PriceChangeOption"] = price_change_option
        if price_increase_option is not None:
            _body["PriceIncreaseOption"] = price_increase_option
        if price_increase_percentage is not None:
            _body["PriceIncreasePercentage"] = price_increase_percentage
        if product_category is not None:
            _body["ProductCategory"] = product_category
        if product_class is not None:
            _body["ProductClass"] = product_class
        if product_family is not None:
            _body["ProductFamily"] = product_family
        if product_line is not None:
            _body["ProductLine"] = product_line
        if revenue_recognition_timing is not None:
            _body["RevenueRecognitionTiming"] = revenue_recognition_timing
        if revenue_amortization_method is not None:
            _body["RevenueAmortizationMethod"] = revenue_amortization_method
        if product_rate_plan_charge_number is not None:
            _body["ProductRatePlanChargeNumber"] = product_rate_plan_charge_number
        if product_rate_plan_charge_tier_data is not None:
            _body["ProductRatePlanChargeTierData"] = product_rate_plan_charge_tier_data
        if product_rate_plan_id is not None:
            _body["ProductRatePlanId"] = product_rate_plan_id
        if rating_group is not None:
            _body["RatingGroup"] = rating_group
        if recognized_revenue_account is not None:
            _body["RecognizedRevenueAccount"] = recognized_revenue_account
        if rev_rec_code is not None:
            _body["RevRecCode"] = rev_rec_code
        if rev_rec_trigger_condition is not None:
            _body["RevRecTriggerCondition"] = rev_rec_trigger_condition
        if revenue_recognition_rule_name is not None:
            _body["RevenueRecognitionRuleName"] = revenue_recognition_rule_name
        if rollover_apply is not None:
            _body["RolloverApply"] = rollover_apply
        if rollover_periods is not None:
            _body["RolloverPeriods"] = rollover_periods
        if smoothing_model is not None:
            _body["SmoothingModel"] = smoothing_model
        if specific_billing_period is not None:
            _body["SpecificBillingPeriod"] = specific_billing_period
        if specific_list_price_base is not None:
            _body["SpecificListPriceBase"] = specific_list_price_base
        if tax_code is not None:
            _body["TaxCode"] = tax_code
        if tax_mode is not None:
            _body["TaxMode"] = tax_mode
        if taxable is not None:
            _body["Taxable"] = taxable
        if trigger_event is not None:
            _body["TriggerEvent"] = trigger_event
        if uom is not None:
            _body["UOM"] = uom
        if up_to_periods is not None:
            _body["UpToPeriods"] = up_to_periods
        if up_to_periods_type is not None:
            _body["UpToPeriodsType"] = up_to_periods_type
        if usage_record_rating_option is not None:
            _body["UsageRecordRatingOption"] = usage_record_rating_option
        if use_discount_specific_accounting_code is not None:
            _body["UseDiscountSpecificAccountingCode"] = use_discount_specific_accounting_code
        if use_tenant_default_for_price_change is not None:
            _body["UseTenantDefaultForPriceChange"] = use_tenant_default_for_price_change
        if validity_period_type is not None:
            _body["ValidityPeriodType"] = validity_period_type
        if weekly_bill_cycle_day is not None:
            _body["WeeklyBillCycleDay"] = weekly_bill_cycle_day
        if apply_to_billing_period_partially is not None:
            _body["ApplyToBillingPeriodPartially"] = apply_to_billing_period_partially
        if rollover_period_length is not None:
            _body["RolloverPeriodLength"] = rollover_period_length
        if formula is not None:
            _body["Formula"] = formula
        if class__ns is not None:
            _body["Class__NS"] = class__ns
        if deferred_rev_account__ns is not None:
            _body["DeferredRevAccount__NS"] = deferred_rev_account__ns
        if department__ns is not None:
            _body["Department__NS"] = department__ns
        if include_children__ns is not None:
            _body["IncludeChildren__NS"] = include_children__ns
        if integration_id__ns is not None:
            _body["IntegrationId__NS"] = integration_id__ns
        if integration_status__ns is not None:
            _body["IntegrationStatus__NS"] = integration_status__ns
        if item_type__ns is not None:
            _body["ItemType__NS"] = item_type__ns
        if location__ns is not None:
            _body["Location__NS"] = location__ns
        if recognized_rev_account__ns is not None:
            _body["RecognizedRevAccount__NS"] = recognized_rev_account__ns
        if rev_rec_end__ns is not None:
            _body["RevRecEnd__NS"] = rev_rec_end__ns
        if rev_rec_start__ns is not None:
            _body["RevRecStart__NS"] = rev_rec_start__ns
        if rev_rec_template_type__ns is not None:
            _body["RevRecTemplateType__NS"] = rev_rec_template_type__ns
        if subsidiary__ns is not None:
            _body["Subsidiary__NS"] = subsidiary__ns
        if sync_date__ns is not None:
            _body["SyncDate__NS"] = sync_date__ns
        args.body = body if body is not None else _body
        if reject_unknown_fields is not None:
            _query_params["rejectUnknownFields"] = reject_unknown_fields
        if accept_encoding is not None:
            _header_params["Accept-Encoding"] = accept_encoding
        if content_encoding is not None:
            _header_params["Content-Encoding"] = content_encoding
        if authorization is not None:
            _header_params["Authorization"] = authorization
        if zuora_entity_ids is not None:
            _header_params["Zuora-Entity-Ids"] = zuora_entity_ids
        if zuora_org_ids is not None:
            _header_params["Zuora-Org-Ids"] = zuora_org_ids
        if zuora_track_id is not None:
            _header_params["Zuora-Track-Id"] = zuora_track_id
        if x_zuora_wsdl_version is not None:
            _header_params["X-Zuora-WSDL-Version"] = x_zuora_wsdl_version
        if id is not None:
            _path_params["id"] = id
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _ap_ut_product_rate_plan_charge_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        CRUD: Update a product rate plan charge
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_reject_unknown_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_accept_encoding,
            request_header_content_encoding,
            request_header_authorization,
            request_header_zuora_entity_ids,
            request_header_zuora_org_ids,
            request_header_zuora_track_id,
            request_header_x_zuora_wsdl_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/object/product-rate-plan-charge/{id}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_proxy_modify_product_rate_plan_charge.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _p_ut_product_rate_plan_charge_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        CRUD: Update a product rate plan charge
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_reject_unknown_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_accept_encoding,
            request_header_content_encoding,
            request_header_authorization,
            request_header_zuora_entity_ids,
            request_header_zuora_org_ids,
            request_header_zuora_track_id,
            request_header_x_zuora_wsdl_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/object/product-rate-plan-charge/{id}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_proxy_modify_product_rate_plan_charge.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class PUtProductRatePlanChargeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ap_ut_product_rate_plan_charge(
        self,
        body: ProxyModifyProductRatePlanCharge,
        id: str,
        accounting_code: typing.Optional[str] = None,
        apply_discount_to: typing.Optional[str] = None,
        bill_cycle_day: typing.Optional[int] = None,
        bill_cycle_type: typing.Optional[str] = None,
        billing_period: typing.Optional[str] = None,
        billing_period_alignment: typing.Optional[str] = None,
        billing_timing: typing.Optional[str] = None,
        charge_function: typing.Optional[str] = None,
        commitment_type: typing.Optional[str] = None,
        charge_model: typing.Optional[str] = None,
        charge_model_configuration: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration] = None,
        credit_option: typing.Optional[str] = None,
        default_quantity: typing.Optional[typing.Union[int, float]] = None,
        deferred_revenue_account: typing.Optional[str] = None,
        delivery_schedule: typing.Optional[ProxyCreateOrModifyDeliverySchedule] = None,
        description: typing.Optional[str] = None,
        discount_level: typing.Optional[str] = None,
        drawdown_rate: typing.Optional[typing.Union[int, float]] = None,
        drawdown_uom: typing.Optional[str] = None,
        end_date_condition: typing.Optional[str] = None,
        exclude_item_billing_from_revenue_accounting: typing.Optional[bool] = None,
        exclude_item_booking_from_revenue_accounting: typing.Optional[bool] = None,
        included_units: typing.Optional[typing.Union[int, float]] = None,
        is_allocation_eligible: typing.Optional[bool] = None,
        is_prepaid: typing.Optional[bool] = None,
        is_rollover: typing.Optional[bool] = None,
        is_stacked_discount: typing.Optional[bool] = None,
        is_unbilled: typing.Optional[bool] = None,
        legacy_revenue_reporting: typing.Optional[bool] = None,
        list_price_base: typing.Optional[str] = None,
        max_quantity: typing.Optional[typing.Union[int, float]] = None,
        min_quantity: typing.Optional[typing.Union[int, float]] = None,
        name: typing.Optional[str] = None,
        number_of_period: typing.Optional[int] = None,
        overage_calculation_option: typing.Optional[typing.Optional[str]] = None,
        overage_unused_units_credit_option: typing.Optional[typing.Optional[str]] = None,
        prepaid_quantity: typing.Optional[typing.Union[int, float]] = None,
        prepaid_uom: typing.Optional[str] = None,
        price_change_option: typing.Optional[typing.Optional[str]] = None,
        price_increase_option: typing.Optional[str] = None,
        price_increase_percentage: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        product_category: typing.Optional[str] = None,
        product_class: typing.Optional[str] = None,
        product_family: typing.Optional[str] = None,
        product_line: typing.Optional[str] = None,
        revenue_recognition_timing: typing.Optional[str] = None,
        revenue_amortization_method: typing.Optional[str] = None,
        product_rate_plan_charge_number: typing.Optional[str] = None,
        product_rate_plan_charge_tier_data: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeTierData] = None,
        product_rate_plan_id: typing.Optional[str] = None,
        rating_group: typing.Optional[typing.Optional[str]] = None,
        recognized_revenue_account: typing.Optional[str] = None,
        rev_rec_code: typing.Optional[typing.Optional[str]] = None,
        rev_rec_trigger_condition: typing.Optional[typing.Optional[str]] = None,
        revenue_recognition_rule_name: typing.Optional[str] = None,
        rollover_apply: typing.Optional[str] = None,
        rollover_periods: typing.Optional[typing.Union[int, float]] = None,
        smoothing_model: typing.Optional[typing.Optional[str]] = None,
        specific_billing_period: typing.Optional[typing.Optional[int]] = None,
        specific_list_price_base: typing.Optional[typing.Optional[int]] = None,
        tax_code: typing.Optional[str] = None,
        tax_mode: typing.Optional[typing.Optional[str]] = None,
        taxable: typing.Optional[bool] = None,
        trigger_event: typing.Optional[str] = None,
        uom: typing.Optional[typing.Optional[str]] = None,
        up_to_periods: typing.Optional[typing.Optional[int]] = None,
        up_to_periods_type: typing.Optional[typing.Optional[str]] = None,
        usage_record_rating_option: typing.Optional[typing.Optional[str]] = None,
        use_discount_specific_accounting_code: typing.Optional[typing.Optional[bool]] = None,
        use_tenant_default_for_price_change: typing.Optional[bool] = None,
        validity_period_type: typing.Optional[str] = None,
        weekly_bill_cycle_day: typing.Optional[str] = None,
        apply_to_billing_period_partially: typing.Optional[bool] = None,
        rollover_period_length: typing.Optional[int] = None,
        formula: typing.Optional[str] = None,
        class__ns: typing.Optional[str] = None,
        deferred_rev_account__ns: typing.Optional[str] = None,
        department__ns: typing.Optional[str] = None,
        include_children__ns: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        item_type__ns: typing.Optional[str] = None,
        location__ns: typing.Optional[str] = None,
        recognized_rev_account__ns: typing.Optional[str] = None,
        rev_rec_end__ns: typing.Optional[str] = None,
        rev_rec_start__ns: typing.Optional[str] = None,
        rev_rec_template_type__ns: typing.Optional[str] = None,
        subsidiary__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        reject_unknown_fields: typing.Optional[bool] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        x_zuora_wsdl_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._p_ut_product_rate_plan_charge_mapped_args(
            body=body,
            id=id,
            accounting_code=accounting_code,
            apply_discount_to=apply_discount_to,
            bill_cycle_day=bill_cycle_day,
            bill_cycle_type=bill_cycle_type,
            billing_period=billing_period,
            billing_period_alignment=billing_period_alignment,
            billing_timing=billing_timing,
            charge_function=charge_function,
            commitment_type=commitment_type,
            charge_model=charge_model,
            charge_model_configuration=charge_model_configuration,
            credit_option=credit_option,
            default_quantity=default_quantity,
            deferred_revenue_account=deferred_revenue_account,
            delivery_schedule=delivery_schedule,
            description=description,
            discount_level=discount_level,
            drawdown_rate=drawdown_rate,
            drawdown_uom=drawdown_uom,
            end_date_condition=end_date_condition,
            exclude_item_billing_from_revenue_accounting=exclude_item_billing_from_revenue_accounting,
            exclude_item_booking_from_revenue_accounting=exclude_item_booking_from_revenue_accounting,
            included_units=included_units,
            is_allocation_eligible=is_allocation_eligible,
            is_prepaid=is_prepaid,
            is_rollover=is_rollover,
            is_stacked_discount=is_stacked_discount,
            is_unbilled=is_unbilled,
            legacy_revenue_reporting=legacy_revenue_reporting,
            list_price_base=list_price_base,
            max_quantity=max_quantity,
            min_quantity=min_quantity,
            name=name,
            number_of_period=number_of_period,
            overage_calculation_option=overage_calculation_option,
            overage_unused_units_credit_option=overage_unused_units_credit_option,
            prepaid_quantity=prepaid_quantity,
            prepaid_uom=prepaid_uom,
            price_change_option=price_change_option,
            price_increase_option=price_increase_option,
            price_increase_percentage=price_increase_percentage,
            product_category=product_category,
            product_class=product_class,
            product_family=product_family,
            product_line=product_line,
            revenue_recognition_timing=revenue_recognition_timing,
            revenue_amortization_method=revenue_amortization_method,
            product_rate_plan_charge_number=product_rate_plan_charge_number,
            product_rate_plan_charge_tier_data=product_rate_plan_charge_tier_data,
            product_rate_plan_id=product_rate_plan_id,
            rating_group=rating_group,
            recognized_revenue_account=recognized_revenue_account,
            rev_rec_code=rev_rec_code,
            rev_rec_trigger_condition=rev_rec_trigger_condition,
            revenue_recognition_rule_name=revenue_recognition_rule_name,
            rollover_apply=rollover_apply,
            rollover_periods=rollover_periods,
            smoothing_model=smoothing_model,
            specific_billing_period=specific_billing_period,
            specific_list_price_base=specific_list_price_base,
            tax_code=tax_code,
            tax_mode=tax_mode,
            taxable=taxable,
            trigger_event=trigger_event,
            uom=uom,
            up_to_periods=up_to_periods,
            up_to_periods_type=up_to_periods_type,
            usage_record_rating_option=usage_record_rating_option,
            use_discount_specific_accounting_code=use_discount_specific_accounting_code,
            use_tenant_default_for_price_change=use_tenant_default_for_price_change,
            validity_period_type=validity_period_type,
            weekly_bill_cycle_day=weekly_bill_cycle_day,
            apply_to_billing_period_partially=apply_to_billing_period_partially,
            rollover_period_length=rollover_period_length,
            formula=formula,
            class__ns=class__ns,
            deferred_rev_account__ns=deferred_rev_account__ns,
            department__ns=department__ns,
            include_children__ns=include_children__ns,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            item_type__ns=item_type__ns,
            location__ns=location__ns,
            recognized_rev_account__ns=recognized_rev_account__ns,
            rev_rec_end__ns=rev_rec_end__ns,
            rev_rec_start__ns=rev_rec_start__ns,
            rev_rec_template_type__ns=rev_rec_template_type__ns,
            subsidiary__ns=subsidiary__ns,
            sync_date__ns=sync_date__ns,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            reject_unknown_fields=reject_unknown_fields,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_track_id=zuora_track_id,
            x_zuora_wsdl_version=x_zuora_wsdl_version,
        )
        return await self._ap_ut_product_rate_plan_charge_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def p_ut_product_rate_plan_charge(
        self,
        body: ProxyModifyProductRatePlanCharge,
        id: str,
        accounting_code: typing.Optional[str] = None,
        apply_discount_to: typing.Optional[str] = None,
        bill_cycle_day: typing.Optional[int] = None,
        bill_cycle_type: typing.Optional[str] = None,
        billing_period: typing.Optional[str] = None,
        billing_period_alignment: typing.Optional[str] = None,
        billing_timing: typing.Optional[str] = None,
        charge_function: typing.Optional[str] = None,
        commitment_type: typing.Optional[str] = None,
        charge_model: typing.Optional[str] = None,
        charge_model_configuration: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration] = None,
        credit_option: typing.Optional[str] = None,
        default_quantity: typing.Optional[typing.Union[int, float]] = None,
        deferred_revenue_account: typing.Optional[str] = None,
        delivery_schedule: typing.Optional[ProxyCreateOrModifyDeliverySchedule] = None,
        description: typing.Optional[str] = None,
        discount_level: typing.Optional[str] = None,
        drawdown_rate: typing.Optional[typing.Union[int, float]] = None,
        drawdown_uom: typing.Optional[str] = None,
        end_date_condition: typing.Optional[str] = None,
        exclude_item_billing_from_revenue_accounting: typing.Optional[bool] = None,
        exclude_item_booking_from_revenue_accounting: typing.Optional[bool] = None,
        included_units: typing.Optional[typing.Union[int, float]] = None,
        is_allocation_eligible: typing.Optional[bool] = None,
        is_prepaid: typing.Optional[bool] = None,
        is_rollover: typing.Optional[bool] = None,
        is_stacked_discount: typing.Optional[bool] = None,
        is_unbilled: typing.Optional[bool] = None,
        legacy_revenue_reporting: typing.Optional[bool] = None,
        list_price_base: typing.Optional[str] = None,
        max_quantity: typing.Optional[typing.Union[int, float]] = None,
        min_quantity: typing.Optional[typing.Union[int, float]] = None,
        name: typing.Optional[str] = None,
        number_of_period: typing.Optional[int] = None,
        overage_calculation_option: typing.Optional[typing.Optional[str]] = None,
        overage_unused_units_credit_option: typing.Optional[typing.Optional[str]] = None,
        prepaid_quantity: typing.Optional[typing.Union[int, float]] = None,
        prepaid_uom: typing.Optional[str] = None,
        price_change_option: typing.Optional[typing.Optional[str]] = None,
        price_increase_option: typing.Optional[str] = None,
        price_increase_percentage: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        product_category: typing.Optional[str] = None,
        product_class: typing.Optional[str] = None,
        product_family: typing.Optional[str] = None,
        product_line: typing.Optional[str] = None,
        revenue_recognition_timing: typing.Optional[str] = None,
        revenue_amortization_method: typing.Optional[str] = None,
        product_rate_plan_charge_number: typing.Optional[str] = None,
        product_rate_plan_charge_tier_data: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeTierData] = None,
        product_rate_plan_id: typing.Optional[str] = None,
        rating_group: typing.Optional[typing.Optional[str]] = None,
        recognized_revenue_account: typing.Optional[str] = None,
        rev_rec_code: typing.Optional[typing.Optional[str]] = None,
        rev_rec_trigger_condition: typing.Optional[typing.Optional[str]] = None,
        revenue_recognition_rule_name: typing.Optional[str] = None,
        rollover_apply: typing.Optional[str] = None,
        rollover_periods: typing.Optional[typing.Union[int, float]] = None,
        smoothing_model: typing.Optional[typing.Optional[str]] = None,
        specific_billing_period: typing.Optional[typing.Optional[int]] = None,
        specific_list_price_base: typing.Optional[typing.Optional[int]] = None,
        tax_code: typing.Optional[str] = None,
        tax_mode: typing.Optional[typing.Optional[str]] = None,
        taxable: typing.Optional[bool] = None,
        trigger_event: typing.Optional[str] = None,
        uom: typing.Optional[typing.Optional[str]] = None,
        up_to_periods: typing.Optional[typing.Optional[int]] = None,
        up_to_periods_type: typing.Optional[typing.Optional[str]] = None,
        usage_record_rating_option: typing.Optional[typing.Optional[str]] = None,
        use_discount_specific_accounting_code: typing.Optional[typing.Optional[bool]] = None,
        use_tenant_default_for_price_change: typing.Optional[bool] = None,
        validity_period_type: typing.Optional[str] = None,
        weekly_bill_cycle_day: typing.Optional[str] = None,
        apply_to_billing_period_partially: typing.Optional[bool] = None,
        rollover_period_length: typing.Optional[int] = None,
        formula: typing.Optional[str] = None,
        class__ns: typing.Optional[str] = None,
        deferred_rev_account__ns: typing.Optional[str] = None,
        department__ns: typing.Optional[str] = None,
        include_children__ns: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        item_type__ns: typing.Optional[str] = None,
        location__ns: typing.Optional[str] = None,
        recognized_rev_account__ns: typing.Optional[str] = None,
        rev_rec_end__ns: typing.Optional[str] = None,
        rev_rec_start__ns: typing.Optional[str] = None,
        rev_rec_template_type__ns: typing.Optional[str] = None,
        subsidiary__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        reject_unknown_fields: typing.Optional[bool] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        x_zuora_wsdl_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._p_ut_product_rate_plan_charge_mapped_args(
            body=body,
            id=id,
            accounting_code=accounting_code,
            apply_discount_to=apply_discount_to,
            bill_cycle_day=bill_cycle_day,
            bill_cycle_type=bill_cycle_type,
            billing_period=billing_period,
            billing_period_alignment=billing_period_alignment,
            billing_timing=billing_timing,
            charge_function=charge_function,
            commitment_type=commitment_type,
            charge_model=charge_model,
            charge_model_configuration=charge_model_configuration,
            credit_option=credit_option,
            default_quantity=default_quantity,
            deferred_revenue_account=deferred_revenue_account,
            delivery_schedule=delivery_schedule,
            description=description,
            discount_level=discount_level,
            drawdown_rate=drawdown_rate,
            drawdown_uom=drawdown_uom,
            end_date_condition=end_date_condition,
            exclude_item_billing_from_revenue_accounting=exclude_item_billing_from_revenue_accounting,
            exclude_item_booking_from_revenue_accounting=exclude_item_booking_from_revenue_accounting,
            included_units=included_units,
            is_allocation_eligible=is_allocation_eligible,
            is_prepaid=is_prepaid,
            is_rollover=is_rollover,
            is_stacked_discount=is_stacked_discount,
            is_unbilled=is_unbilled,
            legacy_revenue_reporting=legacy_revenue_reporting,
            list_price_base=list_price_base,
            max_quantity=max_quantity,
            min_quantity=min_quantity,
            name=name,
            number_of_period=number_of_period,
            overage_calculation_option=overage_calculation_option,
            overage_unused_units_credit_option=overage_unused_units_credit_option,
            prepaid_quantity=prepaid_quantity,
            prepaid_uom=prepaid_uom,
            price_change_option=price_change_option,
            price_increase_option=price_increase_option,
            price_increase_percentage=price_increase_percentage,
            product_category=product_category,
            product_class=product_class,
            product_family=product_family,
            product_line=product_line,
            revenue_recognition_timing=revenue_recognition_timing,
            revenue_amortization_method=revenue_amortization_method,
            product_rate_plan_charge_number=product_rate_plan_charge_number,
            product_rate_plan_charge_tier_data=product_rate_plan_charge_tier_data,
            product_rate_plan_id=product_rate_plan_id,
            rating_group=rating_group,
            recognized_revenue_account=recognized_revenue_account,
            rev_rec_code=rev_rec_code,
            rev_rec_trigger_condition=rev_rec_trigger_condition,
            revenue_recognition_rule_name=revenue_recognition_rule_name,
            rollover_apply=rollover_apply,
            rollover_periods=rollover_periods,
            smoothing_model=smoothing_model,
            specific_billing_period=specific_billing_period,
            specific_list_price_base=specific_list_price_base,
            tax_code=tax_code,
            tax_mode=tax_mode,
            taxable=taxable,
            trigger_event=trigger_event,
            uom=uom,
            up_to_periods=up_to_periods,
            up_to_periods_type=up_to_periods_type,
            usage_record_rating_option=usage_record_rating_option,
            use_discount_specific_accounting_code=use_discount_specific_accounting_code,
            use_tenant_default_for_price_change=use_tenant_default_for_price_change,
            validity_period_type=validity_period_type,
            weekly_bill_cycle_day=weekly_bill_cycle_day,
            apply_to_billing_period_partially=apply_to_billing_period_partially,
            rollover_period_length=rollover_period_length,
            formula=formula,
            class__ns=class__ns,
            deferred_rev_account__ns=deferred_rev_account__ns,
            department__ns=department__ns,
            include_children__ns=include_children__ns,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            item_type__ns=item_type__ns,
            location__ns=location__ns,
            recognized_rev_account__ns=recognized_rev_account__ns,
            rev_rec_end__ns=rev_rec_end__ns,
            rev_rec_start__ns=rev_rec_start__ns,
            rev_rec_template_type__ns=rev_rec_template_type__ns,
            subsidiary__ns=subsidiary__ns,
            sync_date__ns=sync_date__ns,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            reject_unknown_fields=reject_unknown_fields,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_track_id=zuora_track_id,
            x_zuora_wsdl_version=x_zuora_wsdl_version,
        )
        return self._p_ut_product_rate_plan_charge_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class PUtProductRatePlanCharge(BaseApi):

    async def ap_ut_product_rate_plan_charge(
        self,
        body: ProxyModifyProductRatePlanCharge,
        id: str,
        accounting_code: typing.Optional[str] = None,
        apply_discount_to: typing.Optional[str] = None,
        bill_cycle_day: typing.Optional[int] = None,
        bill_cycle_type: typing.Optional[str] = None,
        billing_period: typing.Optional[str] = None,
        billing_period_alignment: typing.Optional[str] = None,
        billing_timing: typing.Optional[str] = None,
        charge_function: typing.Optional[str] = None,
        commitment_type: typing.Optional[str] = None,
        charge_model: typing.Optional[str] = None,
        charge_model_configuration: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration] = None,
        credit_option: typing.Optional[str] = None,
        default_quantity: typing.Optional[typing.Union[int, float]] = None,
        deferred_revenue_account: typing.Optional[str] = None,
        delivery_schedule: typing.Optional[ProxyCreateOrModifyDeliverySchedule] = None,
        description: typing.Optional[str] = None,
        discount_level: typing.Optional[str] = None,
        drawdown_rate: typing.Optional[typing.Union[int, float]] = None,
        drawdown_uom: typing.Optional[str] = None,
        end_date_condition: typing.Optional[str] = None,
        exclude_item_billing_from_revenue_accounting: typing.Optional[bool] = None,
        exclude_item_booking_from_revenue_accounting: typing.Optional[bool] = None,
        included_units: typing.Optional[typing.Union[int, float]] = None,
        is_allocation_eligible: typing.Optional[bool] = None,
        is_prepaid: typing.Optional[bool] = None,
        is_rollover: typing.Optional[bool] = None,
        is_stacked_discount: typing.Optional[bool] = None,
        is_unbilled: typing.Optional[bool] = None,
        legacy_revenue_reporting: typing.Optional[bool] = None,
        list_price_base: typing.Optional[str] = None,
        max_quantity: typing.Optional[typing.Union[int, float]] = None,
        min_quantity: typing.Optional[typing.Union[int, float]] = None,
        name: typing.Optional[str] = None,
        number_of_period: typing.Optional[int] = None,
        overage_calculation_option: typing.Optional[typing.Optional[str]] = None,
        overage_unused_units_credit_option: typing.Optional[typing.Optional[str]] = None,
        prepaid_quantity: typing.Optional[typing.Union[int, float]] = None,
        prepaid_uom: typing.Optional[str] = None,
        price_change_option: typing.Optional[typing.Optional[str]] = None,
        price_increase_option: typing.Optional[str] = None,
        price_increase_percentage: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        product_category: typing.Optional[str] = None,
        product_class: typing.Optional[str] = None,
        product_family: typing.Optional[str] = None,
        product_line: typing.Optional[str] = None,
        revenue_recognition_timing: typing.Optional[str] = None,
        revenue_amortization_method: typing.Optional[str] = None,
        product_rate_plan_charge_number: typing.Optional[str] = None,
        product_rate_plan_charge_tier_data: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeTierData] = None,
        product_rate_plan_id: typing.Optional[str] = None,
        rating_group: typing.Optional[typing.Optional[str]] = None,
        recognized_revenue_account: typing.Optional[str] = None,
        rev_rec_code: typing.Optional[typing.Optional[str]] = None,
        rev_rec_trigger_condition: typing.Optional[typing.Optional[str]] = None,
        revenue_recognition_rule_name: typing.Optional[str] = None,
        rollover_apply: typing.Optional[str] = None,
        rollover_periods: typing.Optional[typing.Union[int, float]] = None,
        smoothing_model: typing.Optional[typing.Optional[str]] = None,
        specific_billing_period: typing.Optional[typing.Optional[int]] = None,
        specific_list_price_base: typing.Optional[typing.Optional[int]] = None,
        tax_code: typing.Optional[str] = None,
        tax_mode: typing.Optional[typing.Optional[str]] = None,
        taxable: typing.Optional[bool] = None,
        trigger_event: typing.Optional[str] = None,
        uom: typing.Optional[typing.Optional[str]] = None,
        up_to_periods: typing.Optional[typing.Optional[int]] = None,
        up_to_periods_type: typing.Optional[typing.Optional[str]] = None,
        usage_record_rating_option: typing.Optional[typing.Optional[str]] = None,
        use_discount_specific_accounting_code: typing.Optional[typing.Optional[bool]] = None,
        use_tenant_default_for_price_change: typing.Optional[bool] = None,
        validity_period_type: typing.Optional[str] = None,
        weekly_bill_cycle_day: typing.Optional[str] = None,
        apply_to_billing_period_partially: typing.Optional[bool] = None,
        rollover_period_length: typing.Optional[int] = None,
        formula: typing.Optional[str] = None,
        class__ns: typing.Optional[str] = None,
        deferred_rev_account__ns: typing.Optional[str] = None,
        department__ns: typing.Optional[str] = None,
        include_children__ns: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        item_type__ns: typing.Optional[str] = None,
        location__ns: typing.Optional[str] = None,
        recognized_rev_account__ns: typing.Optional[str] = None,
        rev_rec_end__ns: typing.Optional[str] = None,
        rev_rec_start__ns: typing.Optional[str] = None,
        rev_rec_template_type__ns: typing.Optional[str] = None,
        subsidiary__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        reject_unknown_fields: typing.Optional[bool] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        x_zuora_wsdl_version: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProxyCreateOrModifyResponsePydantic:
        raw_response = await self.raw.ap_ut_product_rate_plan_charge(
            body=body,
            id=id,
            accounting_code=accounting_code,
            apply_discount_to=apply_discount_to,
            bill_cycle_day=bill_cycle_day,
            bill_cycle_type=bill_cycle_type,
            billing_period=billing_period,
            billing_period_alignment=billing_period_alignment,
            billing_timing=billing_timing,
            charge_function=charge_function,
            commitment_type=commitment_type,
            charge_model=charge_model,
            charge_model_configuration=charge_model_configuration,
            credit_option=credit_option,
            default_quantity=default_quantity,
            deferred_revenue_account=deferred_revenue_account,
            delivery_schedule=delivery_schedule,
            description=description,
            discount_level=discount_level,
            drawdown_rate=drawdown_rate,
            drawdown_uom=drawdown_uom,
            end_date_condition=end_date_condition,
            exclude_item_billing_from_revenue_accounting=exclude_item_billing_from_revenue_accounting,
            exclude_item_booking_from_revenue_accounting=exclude_item_booking_from_revenue_accounting,
            included_units=included_units,
            is_allocation_eligible=is_allocation_eligible,
            is_prepaid=is_prepaid,
            is_rollover=is_rollover,
            is_stacked_discount=is_stacked_discount,
            is_unbilled=is_unbilled,
            legacy_revenue_reporting=legacy_revenue_reporting,
            list_price_base=list_price_base,
            max_quantity=max_quantity,
            min_quantity=min_quantity,
            name=name,
            number_of_period=number_of_period,
            overage_calculation_option=overage_calculation_option,
            overage_unused_units_credit_option=overage_unused_units_credit_option,
            prepaid_quantity=prepaid_quantity,
            prepaid_uom=prepaid_uom,
            price_change_option=price_change_option,
            price_increase_option=price_increase_option,
            price_increase_percentage=price_increase_percentage,
            product_category=product_category,
            product_class=product_class,
            product_family=product_family,
            product_line=product_line,
            revenue_recognition_timing=revenue_recognition_timing,
            revenue_amortization_method=revenue_amortization_method,
            product_rate_plan_charge_number=product_rate_plan_charge_number,
            product_rate_plan_charge_tier_data=product_rate_plan_charge_tier_data,
            product_rate_plan_id=product_rate_plan_id,
            rating_group=rating_group,
            recognized_revenue_account=recognized_revenue_account,
            rev_rec_code=rev_rec_code,
            rev_rec_trigger_condition=rev_rec_trigger_condition,
            revenue_recognition_rule_name=revenue_recognition_rule_name,
            rollover_apply=rollover_apply,
            rollover_periods=rollover_periods,
            smoothing_model=smoothing_model,
            specific_billing_period=specific_billing_period,
            specific_list_price_base=specific_list_price_base,
            tax_code=tax_code,
            tax_mode=tax_mode,
            taxable=taxable,
            trigger_event=trigger_event,
            uom=uom,
            up_to_periods=up_to_periods,
            up_to_periods_type=up_to_periods_type,
            usage_record_rating_option=usage_record_rating_option,
            use_discount_specific_accounting_code=use_discount_specific_accounting_code,
            use_tenant_default_for_price_change=use_tenant_default_for_price_change,
            validity_period_type=validity_period_type,
            weekly_bill_cycle_day=weekly_bill_cycle_day,
            apply_to_billing_period_partially=apply_to_billing_period_partially,
            rollover_period_length=rollover_period_length,
            formula=formula,
            class__ns=class__ns,
            deferred_rev_account__ns=deferred_rev_account__ns,
            department__ns=department__ns,
            include_children__ns=include_children__ns,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            item_type__ns=item_type__ns,
            location__ns=location__ns,
            recognized_rev_account__ns=recognized_rev_account__ns,
            rev_rec_end__ns=rev_rec_end__ns,
            rev_rec_start__ns=rev_rec_start__ns,
            rev_rec_template_type__ns=rev_rec_template_type__ns,
            subsidiary__ns=subsidiary__ns,
            sync_date__ns=sync_date__ns,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            reject_unknown_fields=reject_unknown_fields,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_track_id=zuora_track_id,
            x_zuora_wsdl_version=x_zuora_wsdl_version,
            **kwargs,
        )
        if validate:
            return ProxyCreateOrModifyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProxyCreateOrModifyResponsePydantic, raw_response.body)
    
    
    def p_ut_product_rate_plan_charge(
        self,
        body: ProxyModifyProductRatePlanCharge,
        id: str,
        accounting_code: typing.Optional[str] = None,
        apply_discount_to: typing.Optional[str] = None,
        bill_cycle_day: typing.Optional[int] = None,
        bill_cycle_type: typing.Optional[str] = None,
        billing_period: typing.Optional[str] = None,
        billing_period_alignment: typing.Optional[str] = None,
        billing_timing: typing.Optional[str] = None,
        charge_function: typing.Optional[str] = None,
        commitment_type: typing.Optional[str] = None,
        charge_model: typing.Optional[str] = None,
        charge_model_configuration: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration] = None,
        credit_option: typing.Optional[str] = None,
        default_quantity: typing.Optional[typing.Union[int, float]] = None,
        deferred_revenue_account: typing.Optional[str] = None,
        delivery_schedule: typing.Optional[ProxyCreateOrModifyDeliverySchedule] = None,
        description: typing.Optional[str] = None,
        discount_level: typing.Optional[str] = None,
        drawdown_rate: typing.Optional[typing.Union[int, float]] = None,
        drawdown_uom: typing.Optional[str] = None,
        end_date_condition: typing.Optional[str] = None,
        exclude_item_billing_from_revenue_accounting: typing.Optional[bool] = None,
        exclude_item_booking_from_revenue_accounting: typing.Optional[bool] = None,
        included_units: typing.Optional[typing.Union[int, float]] = None,
        is_allocation_eligible: typing.Optional[bool] = None,
        is_prepaid: typing.Optional[bool] = None,
        is_rollover: typing.Optional[bool] = None,
        is_stacked_discount: typing.Optional[bool] = None,
        is_unbilled: typing.Optional[bool] = None,
        legacy_revenue_reporting: typing.Optional[bool] = None,
        list_price_base: typing.Optional[str] = None,
        max_quantity: typing.Optional[typing.Union[int, float]] = None,
        min_quantity: typing.Optional[typing.Union[int, float]] = None,
        name: typing.Optional[str] = None,
        number_of_period: typing.Optional[int] = None,
        overage_calculation_option: typing.Optional[typing.Optional[str]] = None,
        overage_unused_units_credit_option: typing.Optional[typing.Optional[str]] = None,
        prepaid_quantity: typing.Optional[typing.Union[int, float]] = None,
        prepaid_uom: typing.Optional[str] = None,
        price_change_option: typing.Optional[typing.Optional[str]] = None,
        price_increase_option: typing.Optional[str] = None,
        price_increase_percentage: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        product_category: typing.Optional[str] = None,
        product_class: typing.Optional[str] = None,
        product_family: typing.Optional[str] = None,
        product_line: typing.Optional[str] = None,
        revenue_recognition_timing: typing.Optional[str] = None,
        revenue_amortization_method: typing.Optional[str] = None,
        product_rate_plan_charge_number: typing.Optional[str] = None,
        product_rate_plan_charge_tier_data: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeTierData] = None,
        product_rate_plan_id: typing.Optional[str] = None,
        rating_group: typing.Optional[typing.Optional[str]] = None,
        recognized_revenue_account: typing.Optional[str] = None,
        rev_rec_code: typing.Optional[typing.Optional[str]] = None,
        rev_rec_trigger_condition: typing.Optional[typing.Optional[str]] = None,
        revenue_recognition_rule_name: typing.Optional[str] = None,
        rollover_apply: typing.Optional[str] = None,
        rollover_periods: typing.Optional[typing.Union[int, float]] = None,
        smoothing_model: typing.Optional[typing.Optional[str]] = None,
        specific_billing_period: typing.Optional[typing.Optional[int]] = None,
        specific_list_price_base: typing.Optional[typing.Optional[int]] = None,
        tax_code: typing.Optional[str] = None,
        tax_mode: typing.Optional[typing.Optional[str]] = None,
        taxable: typing.Optional[bool] = None,
        trigger_event: typing.Optional[str] = None,
        uom: typing.Optional[typing.Optional[str]] = None,
        up_to_periods: typing.Optional[typing.Optional[int]] = None,
        up_to_periods_type: typing.Optional[typing.Optional[str]] = None,
        usage_record_rating_option: typing.Optional[typing.Optional[str]] = None,
        use_discount_specific_accounting_code: typing.Optional[typing.Optional[bool]] = None,
        use_tenant_default_for_price_change: typing.Optional[bool] = None,
        validity_period_type: typing.Optional[str] = None,
        weekly_bill_cycle_day: typing.Optional[str] = None,
        apply_to_billing_period_partially: typing.Optional[bool] = None,
        rollover_period_length: typing.Optional[int] = None,
        formula: typing.Optional[str] = None,
        class__ns: typing.Optional[str] = None,
        deferred_rev_account__ns: typing.Optional[str] = None,
        department__ns: typing.Optional[str] = None,
        include_children__ns: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        item_type__ns: typing.Optional[str] = None,
        location__ns: typing.Optional[str] = None,
        recognized_rev_account__ns: typing.Optional[str] = None,
        rev_rec_end__ns: typing.Optional[str] = None,
        rev_rec_start__ns: typing.Optional[str] = None,
        rev_rec_template_type__ns: typing.Optional[str] = None,
        subsidiary__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        reject_unknown_fields: typing.Optional[bool] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        x_zuora_wsdl_version: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ProxyCreateOrModifyResponsePydantic:
        raw_response = self.raw.p_ut_product_rate_plan_charge(
            body=body,
            id=id,
            accounting_code=accounting_code,
            apply_discount_to=apply_discount_to,
            bill_cycle_day=bill_cycle_day,
            bill_cycle_type=bill_cycle_type,
            billing_period=billing_period,
            billing_period_alignment=billing_period_alignment,
            billing_timing=billing_timing,
            charge_function=charge_function,
            commitment_type=commitment_type,
            charge_model=charge_model,
            charge_model_configuration=charge_model_configuration,
            credit_option=credit_option,
            default_quantity=default_quantity,
            deferred_revenue_account=deferred_revenue_account,
            delivery_schedule=delivery_schedule,
            description=description,
            discount_level=discount_level,
            drawdown_rate=drawdown_rate,
            drawdown_uom=drawdown_uom,
            end_date_condition=end_date_condition,
            exclude_item_billing_from_revenue_accounting=exclude_item_billing_from_revenue_accounting,
            exclude_item_booking_from_revenue_accounting=exclude_item_booking_from_revenue_accounting,
            included_units=included_units,
            is_allocation_eligible=is_allocation_eligible,
            is_prepaid=is_prepaid,
            is_rollover=is_rollover,
            is_stacked_discount=is_stacked_discount,
            is_unbilled=is_unbilled,
            legacy_revenue_reporting=legacy_revenue_reporting,
            list_price_base=list_price_base,
            max_quantity=max_quantity,
            min_quantity=min_quantity,
            name=name,
            number_of_period=number_of_period,
            overage_calculation_option=overage_calculation_option,
            overage_unused_units_credit_option=overage_unused_units_credit_option,
            prepaid_quantity=prepaid_quantity,
            prepaid_uom=prepaid_uom,
            price_change_option=price_change_option,
            price_increase_option=price_increase_option,
            price_increase_percentage=price_increase_percentage,
            product_category=product_category,
            product_class=product_class,
            product_family=product_family,
            product_line=product_line,
            revenue_recognition_timing=revenue_recognition_timing,
            revenue_amortization_method=revenue_amortization_method,
            product_rate_plan_charge_number=product_rate_plan_charge_number,
            product_rate_plan_charge_tier_data=product_rate_plan_charge_tier_data,
            product_rate_plan_id=product_rate_plan_id,
            rating_group=rating_group,
            recognized_revenue_account=recognized_revenue_account,
            rev_rec_code=rev_rec_code,
            rev_rec_trigger_condition=rev_rec_trigger_condition,
            revenue_recognition_rule_name=revenue_recognition_rule_name,
            rollover_apply=rollover_apply,
            rollover_periods=rollover_periods,
            smoothing_model=smoothing_model,
            specific_billing_period=specific_billing_period,
            specific_list_price_base=specific_list_price_base,
            tax_code=tax_code,
            tax_mode=tax_mode,
            taxable=taxable,
            trigger_event=trigger_event,
            uom=uom,
            up_to_periods=up_to_periods,
            up_to_periods_type=up_to_periods_type,
            usage_record_rating_option=usage_record_rating_option,
            use_discount_specific_accounting_code=use_discount_specific_accounting_code,
            use_tenant_default_for_price_change=use_tenant_default_for_price_change,
            validity_period_type=validity_period_type,
            weekly_bill_cycle_day=weekly_bill_cycle_day,
            apply_to_billing_period_partially=apply_to_billing_period_partially,
            rollover_period_length=rollover_period_length,
            formula=formula,
            class__ns=class__ns,
            deferred_rev_account__ns=deferred_rev_account__ns,
            department__ns=department__ns,
            include_children__ns=include_children__ns,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            item_type__ns=item_type__ns,
            location__ns=location__ns,
            recognized_rev_account__ns=recognized_rev_account__ns,
            rev_rec_end__ns=rev_rec_end__ns,
            rev_rec_start__ns=rev_rec_start__ns,
            rev_rec_template_type__ns=rev_rec_template_type__ns,
            subsidiary__ns=subsidiary__ns,
            sync_date__ns=sync_date__ns,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            reject_unknown_fields=reject_unknown_fields,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_track_id=zuora_track_id,
            x_zuora_wsdl_version=x_zuora_wsdl_version,
        )
        if validate:
            return ProxyCreateOrModifyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProxyCreateOrModifyResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        body: ProxyModifyProductRatePlanCharge,
        id: str,
        accounting_code: typing.Optional[str] = None,
        apply_discount_to: typing.Optional[str] = None,
        bill_cycle_day: typing.Optional[int] = None,
        bill_cycle_type: typing.Optional[str] = None,
        billing_period: typing.Optional[str] = None,
        billing_period_alignment: typing.Optional[str] = None,
        billing_timing: typing.Optional[str] = None,
        charge_function: typing.Optional[str] = None,
        commitment_type: typing.Optional[str] = None,
        charge_model: typing.Optional[str] = None,
        charge_model_configuration: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration] = None,
        credit_option: typing.Optional[str] = None,
        default_quantity: typing.Optional[typing.Union[int, float]] = None,
        deferred_revenue_account: typing.Optional[str] = None,
        delivery_schedule: typing.Optional[ProxyCreateOrModifyDeliverySchedule] = None,
        description: typing.Optional[str] = None,
        discount_level: typing.Optional[str] = None,
        drawdown_rate: typing.Optional[typing.Union[int, float]] = None,
        drawdown_uom: typing.Optional[str] = None,
        end_date_condition: typing.Optional[str] = None,
        exclude_item_billing_from_revenue_accounting: typing.Optional[bool] = None,
        exclude_item_booking_from_revenue_accounting: typing.Optional[bool] = None,
        included_units: typing.Optional[typing.Union[int, float]] = None,
        is_allocation_eligible: typing.Optional[bool] = None,
        is_prepaid: typing.Optional[bool] = None,
        is_rollover: typing.Optional[bool] = None,
        is_stacked_discount: typing.Optional[bool] = None,
        is_unbilled: typing.Optional[bool] = None,
        legacy_revenue_reporting: typing.Optional[bool] = None,
        list_price_base: typing.Optional[str] = None,
        max_quantity: typing.Optional[typing.Union[int, float]] = None,
        min_quantity: typing.Optional[typing.Union[int, float]] = None,
        name: typing.Optional[str] = None,
        number_of_period: typing.Optional[int] = None,
        overage_calculation_option: typing.Optional[typing.Optional[str]] = None,
        overage_unused_units_credit_option: typing.Optional[typing.Optional[str]] = None,
        prepaid_quantity: typing.Optional[typing.Union[int, float]] = None,
        prepaid_uom: typing.Optional[str] = None,
        price_change_option: typing.Optional[typing.Optional[str]] = None,
        price_increase_option: typing.Optional[str] = None,
        price_increase_percentage: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        product_category: typing.Optional[str] = None,
        product_class: typing.Optional[str] = None,
        product_family: typing.Optional[str] = None,
        product_line: typing.Optional[str] = None,
        revenue_recognition_timing: typing.Optional[str] = None,
        revenue_amortization_method: typing.Optional[str] = None,
        product_rate_plan_charge_number: typing.Optional[str] = None,
        product_rate_plan_charge_tier_data: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeTierData] = None,
        product_rate_plan_id: typing.Optional[str] = None,
        rating_group: typing.Optional[typing.Optional[str]] = None,
        recognized_revenue_account: typing.Optional[str] = None,
        rev_rec_code: typing.Optional[typing.Optional[str]] = None,
        rev_rec_trigger_condition: typing.Optional[typing.Optional[str]] = None,
        revenue_recognition_rule_name: typing.Optional[str] = None,
        rollover_apply: typing.Optional[str] = None,
        rollover_periods: typing.Optional[typing.Union[int, float]] = None,
        smoothing_model: typing.Optional[typing.Optional[str]] = None,
        specific_billing_period: typing.Optional[typing.Optional[int]] = None,
        specific_list_price_base: typing.Optional[typing.Optional[int]] = None,
        tax_code: typing.Optional[str] = None,
        tax_mode: typing.Optional[typing.Optional[str]] = None,
        taxable: typing.Optional[bool] = None,
        trigger_event: typing.Optional[str] = None,
        uom: typing.Optional[typing.Optional[str]] = None,
        up_to_periods: typing.Optional[typing.Optional[int]] = None,
        up_to_periods_type: typing.Optional[typing.Optional[str]] = None,
        usage_record_rating_option: typing.Optional[typing.Optional[str]] = None,
        use_discount_specific_accounting_code: typing.Optional[typing.Optional[bool]] = None,
        use_tenant_default_for_price_change: typing.Optional[bool] = None,
        validity_period_type: typing.Optional[str] = None,
        weekly_bill_cycle_day: typing.Optional[str] = None,
        apply_to_billing_period_partially: typing.Optional[bool] = None,
        rollover_period_length: typing.Optional[int] = None,
        formula: typing.Optional[str] = None,
        class__ns: typing.Optional[str] = None,
        deferred_rev_account__ns: typing.Optional[str] = None,
        department__ns: typing.Optional[str] = None,
        include_children__ns: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        item_type__ns: typing.Optional[str] = None,
        location__ns: typing.Optional[str] = None,
        recognized_rev_account__ns: typing.Optional[str] = None,
        rev_rec_end__ns: typing.Optional[str] = None,
        rev_rec_start__ns: typing.Optional[str] = None,
        rev_rec_template_type__ns: typing.Optional[str] = None,
        subsidiary__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        reject_unknown_fields: typing.Optional[bool] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        x_zuora_wsdl_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._p_ut_product_rate_plan_charge_mapped_args(
            body=body,
            id=id,
            accounting_code=accounting_code,
            apply_discount_to=apply_discount_to,
            bill_cycle_day=bill_cycle_day,
            bill_cycle_type=bill_cycle_type,
            billing_period=billing_period,
            billing_period_alignment=billing_period_alignment,
            billing_timing=billing_timing,
            charge_function=charge_function,
            commitment_type=commitment_type,
            charge_model=charge_model,
            charge_model_configuration=charge_model_configuration,
            credit_option=credit_option,
            default_quantity=default_quantity,
            deferred_revenue_account=deferred_revenue_account,
            delivery_schedule=delivery_schedule,
            description=description,
            discount_level=discount_level,
            drawdown_rate=drawdown_rate,
            drawdown_uom=drawdown_uom,
            end_date_condition=end_date_condition,
            exclude_item_billing_from_revenue_accounting=exclude_item_billing_from_revenue_accounting,
            exclude_item_booking_from_revenue_accounting=exclude_item_booking_from_revenue_accounting,
            included_units=included_units,
            is_allocation_eligible=is_allocation_eligible,
            is_prepaid=is_prepaid,
            is_rollover=is_rollover,
            is_stacked_discount=is_stacked_discount,
            is_unbilled=is_unbilled,
            legacy_revenue_reporting=legacy_revenue_reporting,
            list_price_base=list_price_base,
            max_quantity=max_quantity,
            min_quantity=min_quantity,
            name=name,
            number_of_period=number_of_period,
            overage_calculation_option=overage_calculation_option,
            overage_unused_units_credit_option=overage_unused_units_credit_option,
            prepaid_quantity=prepaid_quantity,
            prepaid_uom=prepaid_uom,
            price_change_option=price_change_option,
            price_increase_option=price_increase_option,
            price_increase_percentage=price_increase_percentage,
            product_category=product_category,
            product_class=product_class,
            product_family=product_family,
            product_line=product_line,
            revenue_recognition_timing=revenue_recognition_timing,
            revenue_amortization_method=revenue_amortization_method,
            product_rate_plan_charge_number=product_rate_plan_charge_number,
            product_rate_plan_charge_tier_data=product_rate_plan_charge_tier_data,
            product_rate_plan_id=product_rate_plan_id,
            rating_group=rating_group,
            recognized_revenue_account=recognized_revenue_account,
            rev_rec_code=rev_rec_code,
            rev_rec_trigger_condition=rev_rec_trigger_condition,
            revenue_recognition_rule_name=revenue_recognition_rule_name,
            rollover_apply=rollover_apply,
            rollover_periods=rollover_periods,
            smoothing_model=smoothing_model,
            specific_billing_period=specific_billing_period,
            specific_list_price_base=specific_list_price_base,
            tax_code=tax_code,
            tax_mode=tax_mode,
            taxable=taxable,
            trigger_event=trigger_event,
            uom=uom,
            up_to_periods=up_to_periods,
            up_to_periods_type=up_to_periods_type,
            usage_record_rating_option=usage_record_rating_option,
            use_discount_specific_accounting_code=use_discount_specific_accounting_code,
            use_tenant_default_for_price_change=use_tenant_default_for_price_change,
            validity_period_type=validity_period_type,
            weekly_bill_cycle_day=weekly_bill_cycle_day,
            apply_to_billing_period_partially=apply_to_billing_period_partially,
            rollover_period_length=rollover_period_length,
            formula=formula,
            class__ns=class__ns,
            deferred_rev_account__ns=deferred_rev_account__ns,
            department__ns=department__ns,
            include_children__ns=include_children__ns,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            item_type__ns=item_type__ns,
            location__ns=location__ns,
            recognized_rev_account__ns=recognized_rev_account__ns,
            rev_rec_end__ns=rev_rec_end__ns,
            rev_rec_start__ns=rev_rec_start__ns,
            rev_rec_template_type__ns=rev_rec_template_type__ns,
            subsidiary__ns=subsidiary__ns,
            sync_date__ns=sync_date__ns,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            reject_unknown_fields=reject_unknown_fields,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_track_id=zuora_track_id,
            x_zuora_wsdl_version=x_zuora_wsdl_version,
        )
        return await self._ap_ut_product_rate_plan_charge_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        body: ProxyModifyProductRatePlanCharge,
        id: str,
        accounting_code: typing.Optional[str] = None,
        apply_discount_to: typing.Optional[str] = None,
        bill_cycle_day: typing.Optional[int] = None,
        bill_cycle_type: typing.Optional[str] = None,
        billing_period: typing.Optional[str] = None,
        billing_period_alignment: typing.Optional[str] = None,
        billing_timing: typing.Optional[str] = None,
        charge_function: typing.Optional[str] = None,
        commitment_type: typing.Optional[str] = None,
        charge_model: typing.Optional[str] = None,
        charge_model_configuration: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeChargeModelConfiguration] = None,
        credit_option: typing.Optional[str] = None,
        default_quantity: typing.Optional[typing.Union[int, float]] = None,
        deferred_revenue_account: typing.Optional[str] = None,
        delivery_schedule: typing.Optional[ProxyCreateOrModifyDeliverySchedule] = None,
        description: typing.Optional[str] = None,
        discount_level: typing.Optional[str] = None,
        drawdown_rate: typing.Optional[typing.Union[int, float]] = None,
        drawdown_uom: typing.Optional[str] = None,
        end_date_condition: typing.Optional[str] = None,
        exclude_item_billing_from_revenue_accounting: typing.Optional[bool] = None,
        exclude_item_booking_from_revenue_accounting: typing.Optional[bool] = None,
        included_units: typing.Optional[typing.Union[int, float]] = None,
        is_allocation_eligible: typing.Optional[bool] = None,
        is_prepaid: typing.Optional[bool] = None,
        is_rollover: typing.Optional[bool] = None,
        is_stacked_discount: typing.Optional[bool] = None,
        is_unbilled: typing.Optional[bool] = None,
        legacy_revenue_reporting: typing.Optional[bool] = None,
        list_price_base: typing.Optional[str] = None,
        max_quantity: typing.Optional[typing.Union[int, float]] = None,
        min_quantity: typing.Optional[typing.Union[int, float]] = None,
        name: typing.Optional[str] = None,
        number_of_period: typing.Optional[int] = None,
        overage_calculation_option: typing.Optional[typing.Optional[str]] = None,
        overage_unused_units_credit_option: typing.Optional[typing.Optional[str]] = None,
        prepaid_quantity: typing.Optional[typing.Union[int, float]] = None,
        prepaid_uom: typing.Optional[str] = None,
        price_change_option: typing.Optional[typing.Optional[str]] = None,
        price_increase_option: typing.Optional[str] = None,
        price_increase_percentage: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        product_category: typing.Optional[str] = None,
        product_class: typing.Optional[str] = None,
        product_family: typing.Optional[str] = None,
        product_line: typing.Optional[str] = None,
        revenue_recognition_timing: typing.Optional[str] = None,
        revenue_amortization_method: typing.Optional[str] = None,
        product_rate_plan_charge_number: typing.Optional[str] = None,
        product_rate_plan_charge_tier_data: typing.Optional[ProxyCreateOrModifyProductRatePlanChargeTierData] = None,
        product_rate_plan_id: typing.Optional[str] = None,
        rating_group: typing.Optional[typing.Optional[str]] = None,
        recognized_revenue_account: typing.Optional[str] = None,
        rev_rec_code: typing.Optional[typing.Optional[str]] = None,
        rev_rec_trigger_condition: typing.Optional[typing.Optional[str]] = None,
        revenue_recognition_rule_name: typing.Optional[str] = None,
        rollover_apply: typing.Optional[str] = None,
        rollover_periods: typing.Optional[typing.Union[int, float]] = None,
        smoothing_model: typing.Optional[typing.Optional[str]] = None,
        specific_billing_period: typing.Optional[typing.Optional[int]] = None,
        specific_list_price_base: typing.Optional[typing.Optional[int]] = None,
        tax_code: typing.Optional[str] = None,
        tax_mode: typing.Optional[typing.Optional[str]] = None,
        taxable: typing.Optional[bool] = None,
        trigger_event: typing.Optional[str] = None,
        uom: typing.Optional[typing.Optional[str]] = None,
        up_to_periods: typing.Optional[typing.Optional[int]] = None,
        up_to_periods_type: typing.Optional[typing.Optional[str]] = None,
        usage_record_rating_option: typing.Optional[typing.Optional[str]] = None,
        use_discount_specific_accounting_code: typing.Optional[typing.Optional[bool]] = None,
        use_tenant_default_for_price_change: typing.Optional[bool] = None,
        validity_period_type: typing.Optional[str] = None,
        weekly_bill_cycle_day: typing.Optional[str] = None,
        apply_to_billing_period_partially: typing.Optional[bool] = None,
        rollover_period_length: typing.Optional[int] = None,
        formula: typing.Optional[str] = None,
        class__ns: typing.Optional[str] = None,
        deferred_rev_account__ns: typing.Optional[str] = None,
        department__ns: typing.Optional[str] = None,
        include_children__ns: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        item_type__ns: typing.Optional[str] = None,
        location__ns: typing.Optional[str] = None,
        recognized_rev_account__ns: typing.Optional[str] = None,
        rev_rec_end__ns: typing.Optional[str] = None,
        rev_rec_start__ns: typing.Optional[str] = None,
        rev_rec_template_type__ns: typing.Optional[str] = None,
        subsidiary__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        reject_unknown_fields: typing.Optional[bool] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        x_zuora_wsdl_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._p_ut_product_rate_plan_charge_mapped_args(
            body=body,
            id=id,
            accounting_code=accounting_code,
            apply_discount_to=apply_discount_to,
            bill_cycle_day=bill_cycle_day,
            bill_cycle_type=bill_cycle_type,
            billing_period=billing_period,
            billing_period_alignment=billing_period_alignment,
            billing_timing=billing_timing,
            charge_function=charge_function,
            commitment_type=commitment_type,
            charge_model=charge_model,
            charge_model_configuration=charge_model_configuration,
            credit_option=credit_option,
            default_quantity=default_quantity,
            deferred_revenue_account=deferred_revenue_account,
            delivery_schedule=delivery_schedule,
            description=description,
            discount_level=discount_level,
            drawdown_rate=drawdown_rate,
            drawdown_uom=drawdown_uom,
            end_date_condition=end_date_condition,
            exclude_item_billing_from_revenue_accounting=exclude_item_billing_from_revenue_accounting,
            exclude_item_booking_from_revenue_accounting=exclude_item_booking_from_revenue_accounting,
            included_units=included_units,
            is_allocation_eligible=is_allocation_eligible,
            is_prepaid=is_prepaid,
            is_rollover=is_rollover,
            is_stacked_discount=is_stacked_discount,
            is_unbilled=is_unbilled,
            legacy_revenue_reporting=legacy_revenue_reporting,
            list_price_base=list_price_base,
            max_quantity=max_quantity,
            min_quantity=min_quantity,
            name=name,
            number_of_period=number_of_period,
            overage_calculation_option=overage_calculation_option,
            overage_unused_units_credit_option=overage_unused_units_credit_option,
            prepaid_quantity=prepaid_quantity,
            prepaid_uom=prepaid_uom,
            price_change_option=price_change_option,
            price_increase_option=price_increase_option,
            price_increase_percentage=price_increase_percentage,
            product_category=product_category,
            product_class=product_class,
            product_family=product_family,
            product_line=product_line,
            revenue_recognition_timing=revenue_recognition_timing,
            revenue_amortization_method=revenue_amortization_method,
            product_rate_plan_charge_number=product_rate_plan_charge_number,
            product_rate_plan_charge_tier_data=product_rate_plan_charge_tier_data,
            product_rate_plan_id=product_rate_plan_id,
            rating_group=rating_group,
            recognized_revenue_account=recognized_revenue_account,
            rev_rec_code=rev_rec_code,
            rev_rec_trigger_condition=rev_rec_trigger_condition,
            revenue_recognition_rule_name=revenue_recognition_rule_name,
            rollover_apply=rollover_apply,
            rollover_periods=rollover_periods,
            smoothing_model=smoothing_model,
            specific_billing_period=specific_billing_period,
            specific_list_price_base=specific_list_price_base,
            tax_code=tax_code,
            tax_mode=tax_mode,
            taxable=taxable,
            trigger_event=trigger_event,
            uom=uom,
            up_to_periods=up_to_periods,
            up_to_periods_type=up_to_periods_type,
            usage_record_rating_option=usage_record_rating_option,
            use_discount_specific_accounting_code=use_discount_specific_accounting_code,
            use_tenant_default_for_price_change=use_tenant_default_for_price_change,
            validity_period_type=validity_period_type,
            weekly_bill_cycle_day=weekly_bill_cycle_day,
            apply_to_billing_period_partially=apply_to_billing_period_partially,
            rollover_period_length=rollover_period_length,
            formula=formula,
            class__ns=class__ns,
            deferred_rev_account__ns=deferred_rev_account__ns,
            department__ns=department__ns,
            include_children__ns=include_children__ns,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            item_type__ns=item_type__ns,
            location__ns=location__ns,
            recognized_rev_account__ns=recognized_rev_account__ns,
            rev_rec_end__ns=rev_rec_end__ns,
            rev_rec_start__ns=rev_rec_start__ns,
            rev_rec_template_type__ns=rev_rec_template_type__ns,
            subsidiary__ns=subsidiary__ns,
            sync_date__ns=sync_date__ns,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            reject_unknown_fields=reject_unknown_fields,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_track_id=zuora_track_id,
            x_zuora_wsdl_version=x_zuora_wsdl_version,
        )
        return self._p_ut_product_rate_plan_charge_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )


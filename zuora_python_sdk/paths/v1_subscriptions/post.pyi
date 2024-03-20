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

from zuora_python_sdk.model.post_subscription_type import POSTSubscriptionType as POSTSubscriptionTypeSchema
from zuora_python_sdk.model.post_subscription_response_type import POSTSubscriptionResponseType as POSTSubscriptionResponseTypeSchema
from zuora_python_sdk.model.post_srp_create_type import POSTSrpCreateType as POSTSrpCreateTypeSchema

from zuora_python_sdk.type.post_srp_create_type import POSTSrpCreateType
from zuora_python_sdk.type.post_subscription_response_type import POSTSubscriptionResponseType
from zuora_python_sdk.type.post_subscription_type import POSTSubscriptionType

from ...api_client import Dictionary
from zuora_python_sdk.pydantic.post_subscription_response_type import POSTSubscriptionResponseType as POSTSubscriptionResponseTypePydantic
from zuora_python_sdk.pydantic.post_subscription_type import POSTSubscriptionType as POSTSubscriptionTypePydantic
from zuora_python_sdk.pydantic.post_srp_create_type import POSTSrpCreateType as POSTSrpCreateTypePydantic

# Header params


class IdempotencyKeySchema(
    schemas.StrSchema
):
    pass
AcceptEncodingSchema = schemas.StrSchema
ContentEncodingSchema = schemas.StrSchema
AuthorizationSchema = schemas.StrSchema


class ZuoraTrackIdSchema(
    schemas.StrSchema
):
    pass
ZuoraEntityIdsSchema = schemas.StrSchema
ZuoraOrgIdsSchema = schemas.StrSchema
ZuoraVersionSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'Idempotency-Key': typing.Union[IdempotencyKeySchema, str, ],
        'Accept-Encoding': typing.Union[AcceptEncodingSchema, str, ],
        'Content-Encoding': typing.Union[ContentEncodingSchema, str, ],
        'Authorization': typing.Union[AuthorizationSchema, str, ],
        'Zuora-Track-Id': typing.Union[ZuoraTrackIdSchema, str, ],
        'Zuora-Entity-Ids': typing.Union[ZuoraEntityIdsSchema, str, ],
        'Zuora-Org-Ids': typing.Union[ZuoraOrgIdsSchema, str, ],
        'zuora-version': typing.Union[ZuoraVersionSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_idempotency_key = api_client.HeaderParameter(
    name="Idempotency-Key",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdempotencyKeySchema,
)
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
request_header_zuora_track_id = api_client.HeaderParameter(
    name="Zuora-Track-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ZuoraTrackIdSchema,
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
request_header_zuora_version = api_client.HeaderParameter(
    name="zuora-version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ZuoraVersionSchema,
)
# body param
SchemaForRequestBodyApplicationJson = POSTSubscriptionTypeSchema


request_body_post_subscription_type = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = POSTSubscriptionResponseTypeSchema
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
    body: POSTSubscriptionResponseType


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: POSTSubscriptionResponseType


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _subscription_mapped_args(
        self,
        body: POSTSubscriptionType,
        account_key: typing.Optional[str] = None,
        application_order: typing.Optional[typing.List[str]] = None,
        apply_credit: typing.Optional[bool] = None,
        apply_credit_balance: typing.Optional[bool] = None,
        auto_renew: typing.Optional[bool] = None,
        collect: typing.Optional[bool] = None,
        contract_effective_date: typing.Optional[date] = None,
        credit_memo_reason_code: typing.Optional[str] = None,
        customer_acceptance_date: typing.Optional[date] = None,
        document_date: typing.Optional[date] = None,
        externally_managed_by: typing.Optional[str] = None,
        gateway_id: typing.Optional[str] = None,
        initial_term: typing.Optional[int] = None,
        initial_term_period_type: typing.Optional[str] = None,
        invoice: typing.Optional[bool] = None,
        invoice_collect: typing.Optional[bool] = None,
        invoice_owner_account_key: typing.Optional[str] = None,
        invoice_separately: typing.Optional[bool] = None,
        invoice_target_date: typing.Optional[date] = None,
        last_booking_date: typing.Optional[date] = None,
        notes: typing.Optional[str] = None,
        payment_method_id: typing.Optional[str] = None,
        prepayment: typing.Optional[bool] = None,
        renewal_setting: typing.Optional[str] = None,
        renewal_term: typing.Optional[int] = None,
        renewal_term_period_type: typing.Optional[str] = None,
        run_billing: typing.Optional[bool] = None,
        service_activation_date: typing.Optional[date] = None,
        subscribe_to_rate_plans: typing.Optional[typing.List[POSTSrpCreateType]] = None,
        subscription_number: typing.Optional[str] = None,
        target_date: typing.Optional[date] = None,
        term_start_date: typing.Optional[date] = None,
        term_type: typing.Optional[str] = None,
        cpq_bundle_json_id__qt: typing.Optional[str] = None,
        opportunity_close_date__qt: typing.Optional[date] = None,
        opportunity_name__qt: typing.Optional[str] = None,
        quote_business_type__qt: typing.Optional[str] = None,
        quote_number__qt: typing.Optional[str] = None,
        quote_type__qt: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        project__ns: typing.Optional[str] = None,
        sales_order__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_version: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if account_key is not None:
            _body["accountKey"] = account_key
        if application_order is not None:
            _body["applicationOrder"] = application_order
        if apply_credit is not None:
            _body["applyCredit"] = apply_credit
        if apply_credit_balance is not None:
            _body["applyCreditBalance"] = apply_credit_balance
        if auto_renew is not None:
            _body["autoRenew"] = auto_renew
        if collect is not None:
            _body["collect"] = collect
        if contract_effective_date is not None:
            _body["contractEffectiveDate"] = contract_effective_date
        if credit_memo_reason_code is not None:
            _body["creditMemoReasonCode"] = credit_memo_reason_code
        if customer_acceptance_date is not None:
            _body["customerAcceptanceDate"] = customer_acceptance_date
        if document_date is not None:
            _body["documentDate"] = document_date
        if externally_managed_by is not None:
            _body["externallyManagedBy"] = externally_managed_by
        if gateway_id is not None:
            _body["gatewayId"] = gateway_id
        if initial_term is not None:
            _body["initialTerm"] = initial_term
        if initial_term_period_type is not None:
            _body["initialTermPeriodType"] = initial_term_period_type
        if invoice is not None:
            _body["invoice"] = invoice
        if invoice_collect is not None:
            _body["invoiceCollect"] = invoice_collect
        if invoice_owner_account_key is not None:
            _body["invoiceOwnerAccountKey"] = invoice_owner_account_key
        if invoice_separately is not None:
            _body["invoiceSeparately"] = invoice_separately
        if invoice_target_date is not None:
            _body["invoiceTargetDate"] = invoice_target_date
        if last_booking_date is not None:
            _body["lastBookingDate"] = last_booking_date
        if notes is not None:
            _body["notes"] = notes
        if payment_method_id is not None:
            _body["paymentMethodId"] = payment_method_id
        if prepayment is not None:
            _body["prepayment"] = prepayment
        if renewal_setting is not None:
            _body["renewalSetting"] = renewal_setting
        if renewal_term is not None:
            _body["renewalTerm"] = renewal_term
        if renewal_term_period_type is not None:
            _body["renewalTermPeriodType"] = renewal_term_period_type
        if run_billing is not None:
            _body["runBilling"] = run_billing
        if service_activation_date is not None:
            _body["serviceActivationDate"] = service_activation_date
        if subscribe_to_rate_plans is not None:
            _body["subscribeToRatePlans"] = subscribe_to_rate_plans
        if subscription_number is not None:
            _body["subscriptionNumber"] = subscription_number
        if target_date is not None:
            _body["targetDate"] = target_date
        if term_start_date is not None:
            _body["termStartDate"] = term_start_date
        if term_type is not None:
            _body["termType"] = term_type
        if cpq_bundle_json_id__qt is not None:
            _body["CpqBundleJsonId__QT"] = cpq_bundle_json_id__qt
        if opportunity_close_date__qt is not None:
            _body["OpportunityCloseDate__QT"] = opportunity_close_date__qt
        if opportunity_name__qt is not None:
            _body["OpportunityName__QT"] = opportunity_name__qt
        if quote_business_type__qt is not None:
            _body["QuoteBusinessType__QT"] = quote_business_type__qt
        if quote_number__qt is not None:
            _body["QuoteNumber__QT"] = quote_number__qt
        if quote_type__qt is not None:
            _body["QuoteType__QT"] = quote_type__qt
        if integration_id__ns is not None:
            _body["IntegrationId__NS"] = integration_id__ns
        if integration_status__ns is not None:
            _body["IntegrationStatus__NS"] = integration_status__ns
        if project__ns is not None:
            _body["Project__NS"] = project__ns
        if sales_order__ns is not None:
            _body["SalesOrder__NS"] = sales_order__ns
        if sync_date__ns is not None:
            _body["SyncDate__NS"] = sync_date__ns
        args.body = body if body is not None else _body
        if idempotency_key is not None:
            _header_params["Idempotency-Key"] = idempotency_key
        if accept_encoding is not None:
            _header_params["Accept-Encoding"] = accept_encoding
        if content_encoding is not None:
            _header_params["Content-Encoding"] = content_encoding
        if authorization is not None:
            _header_params["Authorization"] = authorization
        if zuora_track_id is not None:
            _header_params["Zuora-Track-Id"] = zuora_track_id
        if zuora_entity_ids is not None:
            _header_params["Zuora-Entity-Ids"] = zuora_entity_ids
        if zuora_org_ids is not None:
            _header_params["Zuora-Org-Ids"] = zuora_org_ids
        if zuora_version is not None:
            _header_params["zuora-version"] = zuora_version
        args.header = _header_params
        return args

    async def _asubscription_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
        Create a subscription
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_idempotency_key,
            request_header_accept_encoding,
            request_header_content_encoding,
            request_header_authorization,
            request_header_zuora_track_id,
            request_header_zuora_entity_ids,
            request_header_zuora_org_ids,
            request_header_zuora_version,
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
        method = 'post'.upper()
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
            path_template='/v1/subscriptions',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_post_subscription_type.serialize(body, content_type)
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


    def _subscription_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
        Create a subscription
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_idempotency_key,
            request_header_accept_encoding,
            request_header_content_encoding,
            request_header_authorization,
            request_header_zuora_track_id,
            request_header_zuora_entity_ids,
            request_header_zuora_org_ids,
            request_header_zuora_version,
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
        method = 'post'.upper()
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
            path_template='/v1/subscriptions',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_post_subscription_type.serialize(body, content_type)
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


class SubscriptionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asubscription(
        self,
        body: POSTSubscriptionType,
        account_key: typing.Optional[str] = None,
        application_order: typing.Optional[typing.List[str]] = None,
        apply_credit: typing.Optional[bool] = None,
        apply_credit_balance: typing.Optional[bool] = None,
        auto_renew: typing.Optional[bool] = None,
        collect: typing.Optional[bool] = None,
        contract_effective_date: typing.Optional[date] = None,
        credit_memo_reason_code: typing.Optional[str] = None,
        customer_acceptance_date: typing.Optional[date] = None,
        document_date: typing.Optional[date] = None,
        externally_managed_by: typing.Optional[str] = None,
        gateway_id: typing.Optional[str] = None,
        initial_term: typing.Optional[int] = None,
        initial_term_period_type: typing.Optional[str] = None,
        invoice: typing.Optional[bool] = None,
        invoice_collect: typing.Optional[bool] = None,
        invoice_owner_account_key: typing.Optional[str] = None,
        invoice_separately: typing.Optional[bool] = None,
        invoice_target_date: typing.Optional[date] = None,
        last_booking_date: typing.Optional[date] = None,
        notes: typing.Optional[str] = None,
        payment_method_id: typing.Optional[str] = None,
        prepayment: typing.Optional[bool] = None,
        renewal_setting: typing.Optional[str] = None,
        renewal_term: typing.Optional[int] = None,
        renewal_term_period_type: typing.Optional[str] = None,
        run_billing: typing.Optional[bool] = None,
        service_activation_date: typing.Optional[date] = None,
        subscribe_to_rate_plans: typing.Optional[typing.List[POSTSrpCreateType]] = None,
        subscription_number: typing.Optional[str] = None,
        target_date: typing.Optional[date] = None,
        term_start_date: typing.Optional[date] = None,
        term_type: typing.Optional[str] = None,
        cpq_bundle_json_id__qt: typing.Optional[str] = None,
        opportunity_close_date__qt: typing.Optional[date] = None,
        opportunity_name__qt: typing.Optional[str] = None,
        quote_business_type__qt: typing.Optional[str] = None,
        quote_number__qt: typing.Optional[str] = None,
        quote_type__qt: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        project__ns: typing.Optional[str] = None,
        sales_order__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._subscription_mapped_args(
            body=body,
            account_key=account_key,
            application_order=application_order,
            apply_credit=apply_credit,
            apply_credit_balance=apply_credit_balance,
            auto_renew=auto_renew,
            collect=collect,
            contract_effective_date=contract_effective_date,
            credit_memo_reason_code=credit_memo_reason_code,
            customer_acceptance_date=customer_acceptance_date,
            document_date=document_date,
            externally_managed_by=externally_managed_by,
            gateway_id=gateway_id,
            initial_term=initial_term,
            initial_term_period_type=initial_term_period_type,
            invoice=invoice,
            invoice_collect=invoice_collect,
            invoice_owner_account_key=invoice_owner_account_key,
            invoice_separately=invoice_separately,
            invoice_target_date=invoice_target_date,
            last_booking_date=last_booking_date,
            notes=notes,
            payment_method_id=payment_method_id,
            prepayment=prepayment,
            renewal_setting=renewal_setting,
            renewal_term=renewal_term,
            renewal_term_period_type=renewal_term_period_type,
            run_billing=run_billing,
            service_activation_date=service_activation_date,
            subscribe_to_rate_plans=subscribe_to_rate_plans,
            subscription_number=subscription_number,
            target_date=target_date,
            term_start_date=term_start_date,
            term_type=term_type,
            cpq_bundle_json_id__qt=cpq_bundle_json_id__qt,
            opportunity_close_date__qt=opportunity_close_date__qt,
            opportunity_name__qt=opportunity_name__qt,
            quote_business_type__qt=quote_business_type__qt,
            quote_number__qt=quote_number__qt,
            quote_type__qt=quote_type__qt,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            project__ns=project__ns,
            sales_order__ns=sales_order__ns,
            sync_date__ns=sync_date__ns,
            idempotency_key=idempotency_key,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            zuora_track_id=zuora_track_id,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_version=zuora_version,
        )
        return await self._asubscription_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def subscription(
        self,
        body: POSTSubscriptionType,
        account_key: typing.Optional[str] = None,
        application_order: typing.Optional[typing.List[str]] = None,
        apply_credit: typing.Optional[bool] = None,
        apply_credit_balance: typing.Optional[bool] = None,
        auto_renew: typing.Optional[bool] = None,
        collect: typing.Optional[bool] = None,
        contract_effective_date: typing.Optional[date] = None,
        credit_memo_reason_code: typing.Optional[str] = None,
        customer_acceptance_date: typing.Optional[date] = None,
        document_date: typing.Optional[date] = None,
        externally_managed_by: typing.Optional[str] = None,
        gateway_id: typing.Optional[str] = None,
        initial_term: typing.Optional[int] = None,
        initial_term_period_type: typing.Optional[str] = None,
        invoice: typing.Optional[bool] = None,
        invoice_collect: typing.Optional[bool] = None,
        invoice_owner_account_key: typing.Optional[str] = None,
        invoice_separately: typing.Optional[bool] = None,
        invoice_target_date: typing.Optional[date] = None,
        last_booking_date: typing.Optional[date] = None,
        notes: typing.Optional[str] = None,
        payment_method_id: typing.Optional[str] = None,
        prepayment: typing.Optional[bool] = None,
        renewal_setting: typing.Optional[str] = None,
        renewal_term: typing.Optional[int] = None,
        renewal_term_period_type: typing.Optional[str] = None,
        run_billing: typing.Optional[bool] = None,
        service_activation_date: typing.Optional[date] = None,
        subscribe_to_rate_plans: typing.Optional[typing.List[POSTSrpCreateType]] = None,
        subscription_number: typing.Optional[str] = None,
        target_date: typing.Optional[date] = None,
        term_start_date: typing.Optional[date] = None,
        term_type: typing.Optional[str] = None,
        cpq_bundle_json_id__qt: typing.Optional[str] = None,
        opportunity_close_date__qt: typing.Optional[date] = None,
        opportunity_name__qt: typing.Optional[str] = None,
        quote_business_type__qt: typing.Optional[str] = None,
        quote_number__qt: typing.Optional[str] = None,
        quote_type__qt: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        project__ns: typing.Optional[str] = None,
        sales_order__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._subscription_mapped_args(
            body=body,
            account_key=account_key,
            application_order=application_order,
            apply_credit=apply_credit,
            apply_credit_balance=apply_credit_balance,
            auto_renew=auto_renew,
            collect=collect,
            contract_effective_date=contract_effective_date,
            credit_memo_reason_code=credit_memo_reason_code,
            customer_acceptance_date=customer_acceptance_date,
            document_date=document_date,
            externally_managed_by=externally_managed_by,
            gateway_id=gateway_id,
            initial_term=initial_term,
            initial_term_period_type=initial_term_period_type,
            invoice=invoice,
            invoice_collect=invoice_collect,
            invoice_owner_account_key=invoice_owner_account_key,
            invoice_separately=invoice_separately,
            invoice_target_date=invoice_target_date,
            last_booking_date=last_booking_date,
            notes=notes,
            payment_method_id=payment_method_id,
            prepayment=prepayment,
            renewal_setting=renewal_setting,
            renewal_term=renewal_term,
            renewal_term_period_type=renewal_term_period_type,
            run_billing=run_billing,
            service_activation_date=service_activation_date,
            subscribe_to_rate_plans=subscribe_to_rate_plans,
            subscription_number=subscription_number,
            target_date=target_date,
            term_start_date=term_start_date,
            term_type=term_type,
            cpq_bundle_json_id__qt=cpq_bundle_json_id__qt,
            opportunity_close_date__qt=opportunity_close_date__qt,
            opportunity_name__qt=opportunity_name__qt,
            quote_business_type__qt=quote_business_type__qt,
            quote_number__qt=quote_number__qt,
            quote_type__qt=quote_type__qt,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            project__ns=project__ns,
            sales_order__ns=sales_order__ns,
            sync_date__ns=sync_date__ns,
            idempotency_key=idempotency_key,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            zuora_track_id=zuora_track_id,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_version=zuora_version,
        )
        return self._subscription_oapg(
            body=args.body,
            header_params=args.header,
        )

class Subscription(BaseApi):

    async def asubscription(
        self,
        body: POSTSubscriptionType,
        account_key: typing.Optional[str] = None,
        application_order: typing.Optional[typing.List[str]] = None,
        apply_credit: typing.Optional[bool] = None,
        apply_credit_balance: typing.Optional[bool] = None,
        auto_renew: typing.Optional[bool] = None,
        collect: typing.Optional[bool] = None,
        contract_effective_date: typing.Optional[date] = None,
        credit_memo_reason_code: typing.Optional[str] = None,
        customer_acceptance_date: typing.Optional[date] = None,
        document_date: typing.Optional[date] = None,
        externally_managed_by: typing.Optional[str] = None,
        gateway_id: typing.Optional[str] = None,
        initial_term: typing.Optional[int] = None,
        initial_term_period_type: typing.Optional[str] = None,
        invoice: typing.Optional[bool] = None,
        invoice_collect: typing.Optional[bool] = None,
        invoice_owner_account_key: typing.Optional[str] = None,
        invoice_separately: typing.Optional[bool] = None,
        invoice_target_date: typing.Optional[date] = None,
        last_booking_date: typing.Optional[date] = None,
        notes: typing.Optional[str] = None,
        payment_method_id: typing.Optional[str] = None,
        prepayment: typing.Optional[bool] = None,
        renewal_setting: typing.Optional[str] = None,
        renewal_term: typing.Optional[int] = None,
        renewal_term_period_type: typing.Optional[str] = None,
        run_billing: typing.Optional[bool] = None,
        service_activation_date: typing.Optional[date] = None,
        subscribe_to_rate_plans: typing.Optional[typing.List[POSTSrpCreateType]] = None,
        subscription_number: typing.Optional[str] = None,
        target_date: typing.Optional[date] = None,
        term_start_date: typing.Optional[date] = None,
        term_type: typing.Optional[str] = None,
        cpq_bundle_json_id__qt: typing.Optional[str] = None,
        opportunity_close_date__qt: typing.Optional[date] = None,
        opportunity_name__qt: typing.Optional[str] = None,
        quote_business_type__qt: typing.Optional[str] = None,
        quote_number__qt: typing.Optional[str] = None,
        quote_type__qt: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        project__ns: typing.Optional[str] = None,
        sales_order__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_version: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> POSTSubscriptionResponseTypePydantic:
        raw_response = await self.raw.asubscription(
            body=body,
            account_key=account_key,
            application_order=application_order,
            apply_credit=apply_credit,
            apply_credit_balance=apply_credit_balance,
            auto_renew=auto_renew,
            collect=collect,
            contract_effective_date=contract_effective_date,
            credit_memo_reason_code=credit_memo_reason_code,
            customer_acceptance_date=customer_acceptance_date,
            document_date=document_date,
            externally_managed_by=externally_managed_by,
            gateway_id=gateway_id,
            initial_term=initial_term,
            initial_term_period_type=initial_term_period_type,
            invoice=invoice,
            invoice_collect=invoice_collect,
            invoice_owner_account_key=invoice_owner_account_key,
            invoice_separately=invoice_separately,
            invoice_target_date=invoice_target_date,
            last_booking_date=last_booking_date,
            notes=notes,
            payment_method_id=payment_method_id,
            prepayment=prepayment,
            renewal_setting=renewal_setting,
            renewal_term=renewal_term,
            renewal_term_period_type=renewal_term_period_type,
            run_billing=run_billing,
            service_activation_date=service_activation_date,
            subscribe_to_rate_plans=subscribe_to_rate_plans,
            subscription_number=subscription_number,
            target_date=target_date,
            term_start_date=term_start_date,
            term_type=term_type,
            cpq_bundle_json_id__qt=cpq_bundle_json_id__qt,
            opportunity_close_date__qt=opportunity_close_date__qt,
            opportunity_name__qt=opportunity_name__qt,
            quote_business_type__qt=quote_business_type__qt,
            quote_number__qt=quote_number__qt,
            quote_type__qt=quote_type__qt,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            project__ns=project__ns,
            sales_order__ns=sales_order__ns,
            sync_date__ns=sync_date__ns,
            idempotency_key=idempotency_key,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            zuora_track_id=zuora_track_id,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_version=zuora_version,
            **kwargs,
        )
        if validate:
            return POSTSubscriptionResponseTypePydantic(**raw_response.body)
        return api_client.construct_model_instance(POSTSubscriptionResponseTypePydantic, raw_response.body)
    
    
    def subscription(
        self,
        body: POSTSubscriptionType,
        account_key: typing.Optional[str] = None,
        application_order: typing.Optional[typing.List[str]] = None,
        apply_credit: typing.Optional[bool] = None,
        apply_credit_balance: typing.Optional[bool] = None,
        auto_renew: typing.Optional[bool] = None,
        collect: typing.Optional[bool] = None,
        contract_effective_date: typing.Optional[date] = None,
        credit_memo_reason_code: typing.Optional[str] = None,
        customer_acceptance_date: typing.Optional[date] = None,
        document_date: typing.Optional[date] = None,
        externally_managed_by: typing.Optional[str] = None,
        gateway_id: typing.Optional[str] = None,
        initial_term: typing.Optional[int] = None,
        initial_term_period_type: typing.Optional[str] = None,
        invoice: typing.Optional[bool] = None,
        invoice_collect: typing.Optional[bool] = None,
        invoice_owner_account_key: typing.Optional[str] = None,
        invoice_separately: typing.Optional[bool] = None,
        invoice_target_date: typing.Optional[date] = None,
        last_booking_date: typing.Optional[date] = None,
        notes: typing.Optional[str] = None,
        payment_method_id: typing.Optional[str] = None,
        prepayment: typing.Optional[bool] = None,
        renewal_setting: typing.Optional[str] = None,
        renewal_term: typing.Optional[int] = None,
        renewal_term_period_type: typing.Optional[str] = None,
        run_billing: typing.Optional[bool] = None,
        service_activation_date: typing.Optional[date] = None,
        subscribe_to_rate_plans: typing.Optional[typing.List[POSTSrpCreateType]] = None,
        subscription_number: typing.Optional[str] = None,
        target_date: typing.Optional[date] = None,
        term_start_date: typing.Optional[date] = None,
        term_type: typing.Optional[str] = None,
        cpq_bundle_json_id__qt: typing.Optional[str] = None,
        opportunity_close_date__qt: typing.Optional[date] = None,
        opportunity_name__qt: typing.Optional[str] = None,
        quote_business_type__qt: typing.Optional[str] = None,
        quote_number__qt: typing.Optional[str] = None,
        quote_type__qt: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        project__ns: typing.Optional[str] = None,
        sales_order__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_version: typing.Optional[str] = None,
        validate: bool = False,
    ) -> POSTSubscriptionResponseTypePydantic:
        raw_response = self.raw.subscription(
            body=body,
            account_key=account_key,
            application_order=application_order,
            apply_credit=apply_credit,
            apply_credit_balance=apply_credit_balance,
            auto_renew=auto_renew,
            collect=collect,
            contract_effective_date=contract_effective_date,
            credit_memo_reason_code=credit_memo_reason_code,
            customer_acceptance_date=customer_acceptance_date,
            document_date=document_date,
            externally_managed_by=externally_managed_by,
            gateway_id=gateway_id,
            initial_term=initial_term,
            initial_term_period_type=initial_term_period_type,
            invoice=invoice,
            invoice_collect=invoice_collect,
            invoice_owner_account_key=invoice_owner_account_key,
            invoice_separately=invoice_separately,
            invoice_target_date=invoice_target_date,
            last_booking_date=last_booking_date,
            notes=notes,
            payment_method_id=payment_method_id,
            prepayment=prepayment,
            renewal_setting=renewal_setting,
            renewal_term=renewal_term,
            renewal_term_period_type=renewal_term_period_type,
            run_billing=run_billing,
            service_activation_date=service_activation_date,
            subscribe_to_rate_plans=subscribe_to_rate_plans,
            subscription_number=subscription_number,
            target_date=target_date,
            term_start_date=term_start_date,
            term_type=term_type,
            cpq_bundle_json_id__qt=cpq_bundle_json_id__qt,
            opportunity_close_date__qt=opportunity_close_date__qt,
            opportunity_name__qt=opportunity_name__qt,
            quote_business_type__qt=quote_business_type__qt,
            quote_number__qt=quote_number__qt,
            quote_type__qt=quote_type__qt,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            project__ns=project__ns,
            sales_order__ns=sales_order__ns,
            sync_date__ns=sync_date__ns,
            idempotency_key=idempotency_key,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            zuora_track_id=zuora_track_id,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_version=zuora_version,
        )
        if validate:
            return POSTSubscriptionResponseTypePydantic(**raw_response.body)
        return api_client.construct_model_instance(POSTSubscriptionResponseTypePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        body: POSTSubscriptionType,
        account_key: typing.Optional[str] = None,
        application_order: typing.Optional[typing.List[str]] = None,
        apply_credit: typing.Optional[bool] = None,
        apply_credit_balance: typing.Optional[bool] = None,
        auto_renew: typing.Optional[bool] = None,
        collect: typing.Optional[bool] = None,
        contract_effective_date: typing.Optional[date] = None,
        credit_memo_reason_code: typing.Optional[str] = None,
        customer_acceptance_date: typing.Optional[date] = None,
        document_date: typing.Optional[date] = None,
        externally_managed_by: typing.Optional[str] = None,
        gateway_id: typing.Optional[str] = None,
        initial_term: typing.Optional[int] = None,
        initial_term_period_type: typing.Optional[str] = None,
        invoice: typing.Optional[bool] = None,
        invoice_collect: typing.Optional[bool] = None,
        invoice_owner_account_key: typing.Optional[str] = None,
        invoice_separately: typing.Optional[bool] = None,
        invoice_target_date: typing.Optional[date] = None,
        last_booking_date: typing.Optional[date] = None,
        notes: typing.Optional[str] = None,
        payment_method_id: typing.Optional[str] = None,
        prepayment: typing.Optional[bool] = None,
        renewal_setting: typing.Optional[str] = None,
        renewal_term: typing.Optional[int] = None,
        renewal_term_period_type: typing.Optional[str] = None,
        run_billing: typing.Optional[bool] = None,
        service_activation_date: typing.Optional[date] = None,
        subscribe_to_rate_plans: typing.Optional[typing.List[POSTSrpCreateType]] = None,
        subscription_number: typing.Optional[str] = None,
        target_date: typing.Optional[date] = None,
        term_start_date: typing.Optional[date] = None,
        term_type: typing.Optional[str] = None,
        cpq_bundle_json_id__qt: typing.Optional[str] = None,
        opportunity_close_date__qt: typing.Optional[date] = None,
        opportunity_name__qt: typing.Optional[str] = None,
        quote_business_type__qt: typing.Optional[str] = None,
        quote_number__qt: typing.Optional[str] = None,
        quote_type__qt: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        project__ns: typing.Optional[str] = None,
        sales_order__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._subscription_mapped_args(
            body=body,
            account_key=account_key,
            application_order=application_order,
            apply_credit=apply_credit,
            apply_credit_balance=apply_credit_balance,
            auto_renew=auto_renew,
            collect=collect,
            contract_effective_date=contract_effective_date,
            credit_memo_reason_code=credit_memo_reason_code,
            customer_acceptance_date=customer_acceptance_date,
            document_date=document_date,
            externally_managed_by=externally_managed_by,
            gateway_id=gateway_id,
            initial_term=initial_term,
            initial_term_period_type=initial_term_period_type,
            invoice=invoice,
            invoice_collect=invoice_collect,
            invoice_owner_account_key=invoice_owner_account_key,
            invoice_separately=invoice_separately,
            invoice_target_date=invoice_target_date,
            last_booking_date=last_booking_date,
            notes=notes,
            payment_method_id=payment_method_id,
            prepayment=prepayment,
            renewal_setting=renewal_setting,
            renewal_term=renewal_term,
            renewal_term_period_type=renewal_term_period_type,
            run_billing=run_billing,
            service_activation_date=service_activation_date,
            subscribe_to_rate_plans=subscribe_to_rate_plans,
            subscription_number=subscription_number,
            target_date=target_date,
            term_start_date=term_start_date,
            term_type=term_type,
            cpq_bundle_json_id__qt=cpq_bundle_json_id__qt,
            opportunity_close_date__qt=opportunity_close_date__qt,
            opportunity_name__qt=opportunity_name__qt,
            quote_business_type__qt=quote_business_type__qt,
            quote_number__qt=quote_number__qt,
            quote_type__qt=quote_type__qt,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            project__ns=project__ns,
            sales_order__ns=sales_order__ns,
            sync_date__ns=sync_date__ns,
            idempotency_key=idempotency_key,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            zuora_track_id=zuora_track_id,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_version=zuora_version,
        )
        return await self._asubscription_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        body: POSTSubscriptionType,
        account_key: typing.Optional[str] = None,
        application_order: typing.Optional[typing.List[str]] = None,
        apply_credit: typing.Optional[bool] = None,
        apply_credit_balance: typing.Optional[bool] = None,
        auto_renew: typing.Optional[bool] = None,
        collect: typing.Optional[bool] = None,
        contract_effective_date: typing.Optional[date] = None,
        credit_memo_reason_code: typing.Optional[str] = None,
        customer_acceptance_date: typing.Optional[date] = None,
        document_date: typing.Optional[date] = None,
        externally_managed_by: typing.Optional[str] = None,
        gateway_id: typing.Optional[str] = None,
        initial_term: typing.Optional[int] = None,
        initial_term_period_type: typing.Optional[str] = None,
        invoice: typing.Optional[bool] = None,
        invoice_collect: typing.Optional[bool] = None,
        invoice_owner_account_key: typing.Optional[str] = None,
        invoice_separately: typing.Optional[bool] = None,
        invoice_target_date: typing.Optional[date] = None,
        last_booking_date: typing.Optional[date] = None,
        notes: typing.Optional[str] = None,
        payment_method_id: typing.Optional[str] = None,
        prepayment: typing.Optional[bool] = None,
        renewal_setting: typing.Optional[str] = None,
        renewal_term: typing.Optional[int] = None,
        renewal_term_period_type: typing.Optional[str] = None,
        run_billing: typing.Optional[bool] = None,
        service_activation_date: typing.Optional[date] = None,
        subscribe_to_rate_plans: typing.Optional[typing.List[POSTSrpCreateType]] = None,
        subscription_number: typing.Optional[str] = None,
        target_date: typing.Optional[date] = None,
        term_start_date: typing.Optional[date] = None,
        term_type: typing.Optional[str] = None,
        cpq_bundle_json_id__qt: typing.Optional[str] = None,
        opportunity_close_date__qt: typing.Optional[date] = None,
        opportunity_name__qt: typing.Optional[str] = None,
        quote_business_type__qt: typing.Optional[str] = None,
        quote_number__qt: typing.Optional[str] = None,
        quote_type__qt: typing.Optional[str] = None,
        integration_id__ns: typing.Optional[str] = None,
        integration_status__ns: typing.Optional[str] = None,
        project__ns: typing.Optional[str] = None,
        sales_order__ns: typing.Optional[str] = None,
        sync_date__ns: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        content_encoding: typing.Optional[str] = None,
        authorization: typing.Optional[str] = None,
        zuora_track_id: typing.Optional[str] = None,
        zuora_entity_ids: typing.Optional[str] = None,
        zuora_org_ids: typing.Optional[str] = None,
        zuora_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._subscription_mapped_args(
            body=body,
            account_key=account_key,
            application_order=application_order,
            apply_credit=apply_credit,
            apply_credit_balance=apply_credit_balance,
            auto_renew=auto_renew,
            collect=collect,
            contract_effective_date=contract_effective_date,
            credit_memo_reason_code=credit_memo_reason_code,
            customer_acceptance_date=customer_acceptance_date,
            document_date=document_date,
            externally_managed_by=externally_managed_by,
            gateway_id=gateway_id,
            initial_term=initial_term,
            initial_term_period_type=initial_term_period_type,
            invoice=invoice,
            invoice_collect=invoice_collect,
            invoice_owner_account_key=invoice_owner_account_key,
            invoice_separately=invoice_separately,
            invoice_target_date=invoice_target_date,
            last_booking_date=last_booking_date,
            notes=notes,
            payment_method_id=payment_method_id,
            prepayment=prepayment,
            renewal_setting=renewal_setting,
            renewal_term=renewal_term,
            renewal_term_period_type=renewal_term_period_type,
            run_billing=run_billing,
            service_activation_date=service_activation_date,
            subscribe_to_rate_plans=subscribe_to_rate_plans,
            subscription_number=subscription_number,
            target_date=target_date,
            term_start_date=term_start_date,
            term_type=term_type,
            cpq_bundle_json_id__qt=cpq_bundle_json_id__qt,
            opportunity_close_date__qt=opportunity_close_date__qt,
            opportunity_name__qt=opportunity_name__qt,
            quote_business_type__qt=quote_business_type__qt,
            quote_number__qt=quote_number__qt,
            quote_type__qt=quote_type__qt,
            integration_id__ns=integration_id__ns,
            integration_status__ns=integration_status__ns,
            project__ns=project__ns,
            sales_order__ns=sales_order__ns,
            sync_date__ns=sync_date__ns,
            idempotency_key=idempotency_key,
            accept_encoding=accept_encoding,
            content_encoding=content_encoding,
            authorization=authorization,
            zuora_track_id=zuora_track_id,
            zuora_entity_ids=zuora_entity_ids,
            zuora_org_ids=zuora_org_ids,
            zuora_version=zuora_version,
        )
        return self._subscription_oapg(
            body=args.body,
            header_params=args.header,
        )

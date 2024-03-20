operation_parameter_map = {
    '/system-health/api-requests/volume-summary-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'startTime'
            },
            {
                'name': 'endTime'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'path'
            },
            {
                'name': 'httpMethod'
            },
        ]
    },
    '/v1/accounting-codes-POST': {
        'parameters': [
            {
                'name': 'glAccountName'
            },
            {
                'name': 'glAccountNumber'
            },
            {
                'name': 'name'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-codes/{ac-id}-GET': {
        'parameters': [
            {
                'name': 'ac-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-codes/{ac-id}-PUT': {
        'parameters': [
            {
                'name': 'ac-id'
            },
            {
                'name': 'glAccountName'
            },
            {
                'name': 'glAccountNumber'
            },
            {
                'name': 'name'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-codes/{ac-id}-DELETE': {
        'parameters': [
            {
                'name': 'ac-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-codes/{ac-id}/activate-PUT': {
        'parameters': [
            {
                'name': 'ac-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-codes-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/accounting-codes/{ac-id}/deactivate-PUT': {
        'parameters': [
            {
                'name': 'ac-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-periods-POST': {
        'parameters': [
            {
                'name': 'endDate'
            },
            {
                'name': 'fiscalYear'
            },
            {
                'name': 'fiscal_quarter'
            },
            {
                'name': 'name'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'organizationLabels'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-periods/{ap-id}-GET': {
        'parameters': [
            {
                'name': 'ap-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-periods/{ap-id}-DELETE': {
        'parameters': [
            {
                'name': 'ap-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-periods-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/accounting-periods/{ap-id}/close-PUT': {
        'parameters': [
            {
                'name': 'ap-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-periods/{ap-id}/pending-close-PUT': {
        'parameters': [
            {
                'name': 'ap-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-periods/{ap-id}/reopen-PUT': {
        'parameters': [
            {
                'name': 'ap-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-periods/{ap-id}/run-trial-balance-PUT': {
        'parameters': [
            {
                'name': 'ap-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounting-periods/{ap-id}-PUT': {
        'parameters': [
            {
                'name': 'ap-id'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'fiscalYear'
            },
            {
                'name': 'fiscal_quarter'
            },
            {
                'name': 'name'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounts-POST': {
        'parameters': [
            {
                'name': 'accountNumber'
            },
            {
                'name': 'additionalEmailAddresses'
            },
            {
                'name': 'applicationOrder'
            },
            {
                'name': 'applyCredit'
            },
            {
                'name': 'applyCreditBalance'
            },
            {
                'name': 'autoPay'
            },
            {
                'name': 'batch'
            },
            {
                'name': 'billCycleDay'
            },
            {
                'name': 'billToContact'
            },
            {
                'name': 'collect'
            },
            {
                'name': 'communicationProfileId'
            },
            {
                'name': 'creditCard'
            },
            {
                'name': 'creditMemoReasonCode'
            },
            {
                'name': 'creditMemoTemplateId'
            },
            {
                'name': 'crmId'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'debitMemoTemplateId'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'einvoiceProfile'
            },
            {
                'name': 'hpmCreditCardPaymentMethodId'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'invoiceCollect'
            },
            {
                'name': 'invoiceDeliveryPrefsEmail'
            },
            {
                'name': 'invoiceDeliveryPrefsPrint'
            },
            {
                'name': 'invoiceTargetDate'
            },
            {
                'name': 'invoiceTemplateId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'organizationLabel'
            },
            {
                'name': 'parentId'
            },
            {
                'name': 'partnerAccount'
            },
            {
                'name': 'paymentGateway'
            },
            {
                'name': 'paymentMethod'
            },
            {
                'name': 'paymentTerm'
            },
            {
                'name': 'profileNumber'
            },
            {
                'name': 'runBilling'
            },
            {
                'name': 'salesRep'
            },
            {
                'name': 'sequenceSetId'
            },
            {
                'name': 'soldToContact'
            },
            {
                'name': 'soldToSameAsBillTo'
            },
            {
                'name': 'subscription'
            },
            {
                'name': 'tagging'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'taxInfo'
            },
            {
                'name': 'Class__NS'
            },
            {
                'name': 'CustomerType__NS'
            },
            {
                'name': 'Department__NS'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Location__NS'
            },
            {
                'name': 'Subsidiary__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'SynctoNetSuite__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/accounts/{account-key}-GET': {
        'parameters': [
            {
                'name': 'account-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounts/{account-key}-PUT': {
        'parameters': [
            {
                'name': 'account-key'
            },
            {
                'name': 'additionalEmailAddresses'
            },
            {
                'name': 'autoPay'
            },
            {
                'name': 'batch'
            },
            {
                'name': 'billCycleDay'
            },
            {
                'name': 'billToContact'
            },
            {
                'name': 'communicationProfileId'
            },
            {
                'name': 'creditMemoTemplateId'
            },
            {
                'name': 'crmId'
            },
            {
                'name': 'customerServiceRepName'
            },
            {
                'name': 'debitMemoTemplateId'
            },
            {
                'name': 'defaultPaymentMethodId'
            },
            {
                'name': 'einvoiceProfile'
            },
            {
                'name': 'invoiceDeliveryPrefsEmail'
            },
            {
                'name': 'invoiceDeliveryPrefsPrint'
            },
            {
                'name': 'invoiceTemplateId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'parentId'
            },
            {
                'name': 'partnerAccount'
            },
            {
                'name': 'paymentGateway'
            },
            {
                'name': 'paymentTerm'
            },
            {
                'name': 'profileNumber'
            },
            {
                'name': 'purchaseOrderNumber'
            },
            {
                'name': 'salesRep'
            },
            {
                'name': 'sequenceSetId'
            },
            {
                'name': 'soldToContact'
            },
            {
                'name': 'tagging'
            },
            {
                'name': 'taxInfo'
            },
            {
                'name': 'Class__NS'
            },
            {
                'name': 'CustomerType__NS'
            },
            {
                'name': 'Department__NS'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Location__NS'
            },
            {
                'name': 'Subsidiary__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'SynctoNetSuite__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounts/{account-key}-DELETE': {
        'parameters': [
            {
                'name': 'account-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounts/{account-key}/summary-GET': {
        'parameters': [
            {
                'name': 'account-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'excludeUsage'
            },
        ]
    },
    '/v1/accounts/{account-key}/payment-methods/default-GET': {
        'parameters': [
            {
                'name': 'account-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounts/{account-key}/payment-methods-GET': {
        'parameters': [
            {
                'name': 'account-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'isDefaultOnly'
            },
            {
                'name': 'isActiveOnly'
            },
        ]
    },
    '/v1/action/create-POST': {
        'parameters': [
            {
                'name': 'objects'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/action/delete-POST': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/action/query-POST': {
        'parameters': [
            {
                'name': 'queryString'
            },
            {
                'name': 'conf'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/action/queryMore-POST': {
        'parameters': [
            {
                'name': 'queryLocator'
            },
            {
                'name': 'conf'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/action/update-POST': {
        'parameters': [
            {
                'name': 'objects'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/batch-query/jobs/{jobid}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'jobid'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/batch-query/jobs/{jobid}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'jobid'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/batch-query-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'version'
            },
            {
                'name': 'dateTimeUtc'
            },
            {
                'name': 'format'
            },
            {
                'name': 'incrementalTime'
            },
            {
                'name': 'name'
            },
            {
                'name': 'notifyUrl'
            },
            {
                'name': 'nullReplacement'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'project'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'sourceData'
            },
            {
                'name': 'useQueryLabels'
            },
            {
                'name': 'warehouseSize'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/batch-query/jobs/partner/{partner}/project/{project}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'partner'
            },
            {
                'name': 'project'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/attachments-POST': {
        'parameters': [
            {
                'name': 'associatedObjectType'
            },
            {
                'name': 'associatedObjectKey'
            },
            {
                'name': 'file'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/v1/attachments/{attachment-id}-GET': {
        'parameters': [
            {
                'name': 'attachment-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/attachments/{attachment-id}-PUT': {
        'parameters': [
            {
                'name': 'attachment-id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'fileName'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/attachments/{attachment-id}-DELETE': {
        'parameters': [
            {
                'name': 'attachment-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/attachments/{object-type}/{object-key}-GET': {
        'parameters': [
            {
                'name': 'object-type'
            },
            {
                'name': 'object-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/bill-runs/{billRunId}-GET': {
        'parameters': [
            {
                'name': 'billRunId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/bill-runs/{billRunId}/cancel-PUT': {
        'parameters': [
            {
                'name': 'billRunId'
            },
            {
                'name': 'cancelOnce'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/bill-runs-POST': {
        'parameters': [
            {
                'name': 'autoEmail'
            },
            {
                'name': 'autoPost'
            },
            {
                'name': 'autoRenewal'
            },
            {
                'name': 'batches'
            },
            {
                'name': 'billCycleDay'
            },
            {
                'name': 'billRunFilters'
            },
            {
                'name': 'billRunType'
            },
            {
                'name': 'chargeTypeToExclude'
            },
            {
                'name': 'invoiceDate'
            },
            {
                'name': 'name'
            },
            {
                'name': 'noEmailForZeroAmountInvoice'
            },
            {
                'name': 'organizationLabels'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/bill-runs/{billRunId}-DELETE': {
        'parameters': [
            {
                'name': 'billRunId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/bill-runs/{billRunKey}/emails-POST': {
        'parameters': [
            {
                'name': 'billRunKey'
            },
            {
                'name': 'resend'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/bill-runs/{billRunId}/post-PUT': {
        'parameters': [
            {
                'name': 'invoiceDate'
            },
            {
                'name': 'billRunId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/system-health/billing-documents/volume-summary-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'startTime'
            },
            {
                'name': 'endTime'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/accounts/billing-documents/files/deletion-jobs-POST': {
        'parameters': [
            {
                'name': 'accountIds'
            },
            {
                'name': 'accountKeys'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/accounts/billing-documents/files/deletion-jobs/{jobId}-GET': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/billing-documents-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'status'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/accounts/{key}/billing-documents/generate-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'autoPost'
            },
            {
                'name': 'autoRenew'
            },
            {
                'name': 'chargeTypeToExclude'
            },
            {
                'name': 'creditMemoReasonCode'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'subscriptionIds'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/billing-preview-runs-POST': {
        'parameters': [
            {
                'name': 'targetDate'
            },
            {
                'name': 'assumeRenewal'
            },
            {
                'name': 'batch'
            },
            {
                'name': 'batches'
            },
            {
                'name': 'chargeTypeToExclude'
            },
            {
                'name': 'includingDraftItems'
            },
            {
                'name': 'includingEvergreenSubscription'
            },
            {
                'name': 'organizationLabels'
            },
            {
                'name': 'storageOption'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/billing-preview-runs/{billingPreviewRunId}-GET': {
        'parameters': [
            {
                'name': 'billingPreviewRunId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/catalog/products-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/catalog/products/{product-key}-GET': {
        'parameters': [
            {
                'name': 'product-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/catalog-groups/{catalog-group-key}-DELETE': {
        'parameters': [
            {
                'name': 'catalog-group-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/catalog-groups-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'productRatePlans'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/catalog-groups-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/catalog-groups/{catalog-group-key}-GET': {
        'parameters': [
            {
                'name': 'catalog-group-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/catalog-groups/{catalog-group-key}-PUT': {
        'parameters': [
            {
                'name': 'catalog-group-key'
            },
            {
                'name': 'description'
            },
            {
                'name': 'add'
            },
            {
                'name': 'name'
            },
            {
                'name': 'remove'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/deployment-manager/deployment_artifacts/compare-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'tenant'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'template'
            },
        ]
    },
    '/deployment-manager/deployment_templates-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'templateTenant'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'content'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'customObjects'
            },
            {
                'name': 'notifications'
            },
            {
                'name': 'selectedComponents'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'workflows'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/deployment-manager/deployment_templates/{id}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/deployment-manager/deployment_templates/{id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/deployment-manager/deployment_artifacts-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'deployment_template_id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/deployment-manager/deployment_artifacts/deploy-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'entityUuid'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sendEmail'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'tenant'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'emailIds'
            },
            {
                'name': 'metaData'
            },
            {
                'name': 'request'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/deployment-manager/deployment_artifacts/retrieve-settings-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/deployment-manager/deployment_templates-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/contact-snapshots/{contact-snapshot-id}-GET': {
        'parameters': [
            {
                'name': 'contact-snapshot-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/contacts/{contactId}-GET': {
        'parameters': [
            {
                'name': 'contactId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/contacts/{contactId}-PUT': {
        'parameters': [
            {
                'name': 'contactId'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'contactDescription'
            },
            {
                'name': 'country'
            },
            {
                'name': 'county'
            },
            {
                'name': 'fax'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'homePhone'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'mobilePhone'
            },
            {
                'name': 'nickname'
            },
            {
                'name': 'otherPhone'
            },
            {
                'name': 'otherPhoneType'
            },
            {
                'name': 'personalEmail'
            },
            {
                'name': 'state'
            },
            {
                'name': 'taxRegion'
            },
            {
                'name': 'workEmail'
            },
            {
                'name': 'workPhone'
            },
            {
                'name': 'zipCode'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/contacts/{contactId}-DELETE': {
        'parameters': [
            {
                'name': 'contactId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/contacts-POST': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'contactDescription'
            },
            {
                'name': 'country'
            },
            {
                'name': 'county'
            },
            {
                'name': 'fax'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'homePhone'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'mobilePhone'
            },
            {
                'name': 'nickname'
            },
            {
                'name': 'otherPhone'
            },
            {
                'name': 'otherPhoneType'
            },
            {
                'name': 'personalEmail'
            },
            {
                'name': 'state'
            },
            {
                'name': 'taxRegion'
            },
            {
                'name': 'workEmail'
            },
            {
                'name': 'workPhone'
            },
            {
                'name': 'zipCode'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/contacts/{contactId}/scrub-PUT': {
        'parameters': [
            {
                'name': 'contactId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/apply-PUT': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'debitMemos'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'invoices'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/cancel-PUT': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/bulk-POST': {
        'parameters': [
            {
                'name': 'sourceType'
            },
            {
                'name': 'memos'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/taxationitems-POST': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'taxationItems'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}-GET': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}-DELETE': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/files-GET': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/creditmemos-POST': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'autoApplyToInvoiceUponPosting'
            },
            {
                'name': 'autoPost'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'excludeFromAutoApplyRules'
            },
            {
                'name': 'invoiceId'
            },
            {
                'name': 'items'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'taxAutoCalculation'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Transaction__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/creditmemos-POST': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'autoPost'
            },
            {
                'name': 'charges'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'customRates'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'excludeFromAutoApplyRules'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Transaction__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/items/{cmitemid}-GET': {
        'parameters': [
            {
                'name': 'cmitemid'
            },
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/items-GET': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'zuora-version'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'appliedAmount'
            },
            {
                'name': 'createdById'
            },
            {
                'name': 'createdDate'
            },
            {
                'name': 'id'
            },
            {
                'name': 'refundAmount'
            },
            {
                'name': 'serviceEndDate'
            },
            {
                'name': 'serviceStartDate'
            },
            {
                'name': 'sku'
            },
            {
                'name': 'skuName'
            },
            {
                'name': 'sourceItemId'
            },
            {
                'name': 'subscriptionId'
            },
            {
                'name': 'updatedById'
            },
            {
                'name': 'updatedDate'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/parts/{partid}-GET': {
        'parameters': [
            {
                'name': 'partid'
            },
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/parts-GET': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/pdfs-POST': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/pdf-status-GET': {
        'parameters': [
            {
                'name': 'creditMemoKeys'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/creditmemos-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'appliedAmount'
            },
            {
                'name': 'autoApplyUponPosting'
            },
            {
                'name': 'createdById'
            },
            {
                'name': 'createdDate'
            },
            {
                'name': 'creditMemoDate'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'excludeFromAutoApplyRules'
            },
            {
                'name': 'number'
            },
            {
                'name': 'referredInvoiceId'
            },
            {
                'name': 'refundAmount'
            },
            {
                'name': 'status'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'taxAmount'
            },
            {
                'name': 'totalTaxExemptAmount'
            },
            {
                'name': 'transferredToAccounting'
            },
            {
                'name': 'unappliedAmount'
            },
            {
                'name': 'updatedById'
            },
            {
                'name': 'updatedDate'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/emails-POST': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'emailAddresses'
            },
            {
                'name': 'includeAdditionalEmailAddresses'
            },
            {
                'name': 'pdfFileId'
            },
            {
                'name': 'useEmailTemplateSetting'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/einvoice/generate-PUT': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/post-PUT': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/refunds-POST': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'customRates'
            },
            {
                'name': 'financeInformation'
            },
            {
                'name': 'gatewayId'
            },
            {
                'name': 'gatewayOptions'
            },
            {
                'name': 'items'
            },
            {
                'name': 'methodType'
            },
            {
                'name': 'paymentMethodId'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'referenceId'
            },
            {
                'name': 'refundDate'
            },
            {
                'name': 'secondRefundReferenceId'
            },
            {
                'name': 'softDescriptor'
            },
            {
                'name': 'softDescriptorPhone'
            },
            {
                'name': 'totalAmount'
            },
            {
                'name': 'type'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'SynctoNetSuite__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/reverse-PUT': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'applyEffectiveDate'
            },
            {
                'name': 'memoDate'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoId}/items/{cmitemid}/taxation-items-GET': {
        'parameters': [
            {
                'name': 'cmitemid'
            },
            {
                'name': 'creditMemoId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/unapply-PUT': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'debitMemos'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'invoices'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/unpost-PUT': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}-PUT': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'autoApplyUponPosting'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'excludeFromAutoApplyRules'
            },
            {
                'name': 'items'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'transferredToAccounting'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Transaction__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/creditmemos/bulk-PUT': {
        'parameters': [
            {
                'name': 'memos'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoKey}/files-POST': {
        'parameters': [
            {
                'name': 'creditMemoKey'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/v1/creditmemos/{creditMemoId}/write-off-PUT': {
        'parameters': [
            {
                'name': 'creditMemoId'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'memoDate'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/events/event-triggers-POST': {
        'parameters': [
            {
                'name': 'active'
            },
            {
                'name': 'baseObject'
            },
            {
                'name': 'condition'
            },
            {
                'name': 'eventType'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'description'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/events/event-triggers/{id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/events/event-triggers/{id}-PUT': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'condition'
            },
            {
                'name': 'eventType'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/events/event-triggers/{id}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/events/event-triggers-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'baseObject'
            },
            {
                'name': 'eventTypeName'
            },
            {
                'name': 'active'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/custom-exchange-rates/{currency}-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/objects/definitions/default-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
            {
                'name': 'select'
            },
        ]
    },
    '/objects/definitions/default/{object}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'object'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/definitions/default/{object}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'object'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/definitions/default-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'definitions'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/migrations-POST': {
        'parameters': [
            {
                'name': 'actions'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/jobs-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/objects/jobs-POST': {
        'parameters': [
            {
                'name': 'namespace'
            },
            {
                'name': 'object'
            },
            {
                'name': 'operation'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/jobs/{id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/jobs/{id}/cancel-PATCH': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/jobs/{id}/errors-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/jobs/{id}/files-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/records/default/{object}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'object'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
            {
                'name': 'q'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/objects/records/default/{object}/{id}-PUT': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'object'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'If-Match'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/records/default/{object}/{id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'object'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/records/default/{object}/{id}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'object'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/records/default/{object}-POST': {
        'parameters': [
            {
                'name': 'records'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'object'
            },
            {
                'name': 'allowPartialSuccess'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/batch/default/{object}-POST': {
        'parameters': [
            {
                'name': 'action'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'object'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/objects/records/default/{object}/{id}-PATCH': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'object'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Version'
            },
        ]
    },
    '/open-payment-method-types-POST': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'internalName'
            },
            {
                'name': 'label'
            },
            {
                'name': 'methodReferenceIdField'
            },
            {
                'name': 'tenantId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'subTypeField'
            },
            {
                'name': 'userReferenceIdField'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/open-payment-method-types/{paymentMethodTypeName}/published-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'paymentMethodTypeName'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/open-payment-method-types/{paymentMethodTypeName}/draft/{revisionNumber}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'paymentMethodTypeName'
            },
            {
                'name': 'revisionNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/open-payment-method-types/publish/{paymentMethodTypeName}-PUT': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'paymentMethodTypeName'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/open-payment-method-types/{paymentMethodTypeName}-PUT': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'internalName'
            },
            {
                'name': 'label'
            },
            {
                'name': 'methodReferenceIdField'
            },
            {
                'name': 'tenantId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'paymentMethodTypeName'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'subTypeField'
            },
            {
                'name': 'userReferenceIdField'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/events/scheduled-events-POST': {
        'parameters': [
            {
                'name': 'apiField'
            },
            {
                'name': 'apiObject'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'minutes'
            },
            {
                'name': 'name'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'description'
            },
            {
                'name': 'parameters'
            },
            {
                'name': 'active'
            },
            {
                'name': 'condition'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/events/scheduled-events/{id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/events/scheduled-events/{id}-PUT': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'parameters'
            },
            {
                'name': 'active'
            },
            {
                'name': 'condition'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'minutes'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/events/scheduled-events/{id}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/events/scheduled-events-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'eventTypeName'
            },
            {
                'name': 'apiObject'
            },
            {
                'name': 'apiField'
            },
            {
                'name': 'active'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/uno/data-backfill/bookingdate/jobs/{jobId}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/uno/data-backfill/bookingdate/jobs-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/uno/data-backfill/jobs-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'file'
            },
            {
                'name': 'checksum'
            },
        ]
    },
    '/v1/uno/data-backfill/jobs/{jobId}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/uno/back-fill/jobs/{type}/template-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/uno/data-backfill/bookingdate/jobs-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/uno/data-backfill/listjobs-GET': {
        'parameters': [
        ]
    },
    '/v1/uno/data-backfill/bookingdate/jobs/{jobId}-PUT': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/uno/data-backfill/jobs/{jobId}-PUT': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/multi-organizations/data-labeling-job-POST': {
        'parameters': [
            {
                'name': 'objectType'
            },
            {
                'name': 'queryType'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'orgIds'
            },
            {
                'name': 'orgs'
            },
            {
                'name': 'query'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/multi-organizations/data-labeling-job/{job-id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'job-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/query/jobs-POST': {
        'parameters': [
            {
                'name': 'compression'
            },
            {
                'name': 'output'
            },
            {
                'name': 'outputFormat'
            },
            {
                'name': 'query'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'columnSeparator'
            },
            {
                'name': 'encryptionKey'
            },
            {
                'name': 'readDeleted'
            },
            {
                'name': 'sourceData'
            },
            {
                'name': 'useIndexJoin'
            },
            {
                'name': 'warehouseSize'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/query/jobs/{job-id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'job-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/query/jobs/{job-id}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'job-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/query/jobs-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'queryStatus'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/cancel-PUT': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/bulk-POST': {
        'parameters': [
            {
                'name': 'sourceType'
            },
            {
                'name': 'memos'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/taxationitems-POST': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'taxationItems'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}-GET': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}-PUT': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'autoPay'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'dueDate'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'items'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'transferredToAccounting'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}-DELETE': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoId}/application-parts-GET': {
        'parameters': [
            {
                'name': 'debitMemoId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/collect-POST': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'applicationOrder'
            },
            {
                'name': 'applyCredit'
            },
            {
                'name': 'collect'
            },
            {
                'name': 'payment'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/files-GET': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/debitmemos-POST': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'autoPay'
            },
            {
                'name': 'autoPost'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'invoiceId'
            },
            {
                'name': 'items'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'taxAutoCalculation'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/debitmemos-POST': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'autoPay'
            },
            {
                'name': 'autoPost'
            },
            {
                'name': 'charges'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'customRates'
            },
            {
                'name': 'dueDate'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/items/{dmitemid}-GET': {
        'parameters': [
            {
                'name': 'dmitemid'
            },
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/items-GET': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'zuora-version'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'beAppliedAmount'
            },
            {
                'name': 'createdById'
            },
            {
                'name': 'createdDate'
            },
            {
                'name': 'id'
            },
            {
                'name': 'serviceEndDate'
            },
            {
                'name': 'serviceStartDate'
            },
            {
                'name': 'sku'
            },
            {
                'name': 'skuName'
            },
            {
                'name': 'sourceItemId'
            },
            {
                'name': 'subscriptionId'
            },
            {
                'name': 'updatedById'
            },
            {
                'name': 'updatedDate'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/pdfs-POST': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/pdf-status-GET': {
        'parameters': [
            {
                'name': 'debitMemoKeys'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/debitmemos-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'balance'
            },
            {
                'name': 'beAppliedAmount'
            },
            {
                'name': 'createdById'
            },
            {
                'name': 'createdDate'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'debitMemoDate'
            },
            {
                'name': 'dueDate'
            },
            {
                'name': 'number'
            },
            {
                'name': 'referredInvoiceId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'taxAmount'
            },
            {
                'name': 'totalTaxExemptAmount'
            },
            {
                'name': 'updatedById'
            },
            {
                'name': 'updatedDate'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/emails-POST': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'emailAddresses'
            },
            {
                'name': 'includeAdditionalEmailAddresses'
            },
            {
                'name': 'pdfFileId'
            },
            {
                'name': 'useEmailTemplateSetting'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/einvoice/generate-PUT': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/post-PUT': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoId}/items/{dmitemid}/taxation-items-GET': {
        'parameters': [
            {
                'name': 'dmitemid'
            },
            {
                'name': 'debitMemoId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/unpost-PUT': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/bulk-PUT': {
        'parameters': [
            {
                'name': 'memos'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/debitmemos-PUT': {
        'parameters': [
            {
                'name': 'debitMemos'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/debitmemos/{debitMemoKey}/files-POST': {
        'parameters': [
            {
                'name': 'debitMemoKey'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/v1/adjustments-POST': {
        'parameters': [
            {
                'name': 'endDate'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'chargeNumbers'
            },
            {
                'name': 'deferredRevenueAccountingCode'
            },
            {
                'name': 'exclusion'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'recognizedRevenueAccountingCode'
            },
            {
                'name': 'revenueRecognitionRuleName'
            },
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/adjustments/preview-POST': {
        'parameters': [
            {
                'name': 'endDate'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'chargeNumbers'
            },
            {
                'name': 'deferredRevenueAccountingCode'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'recognizedRevenueAccountingCode'
            },
            {
                'name': 'revenueRecognitionRuleName'
            },
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/adjustments/{adjustment-key}-GET': {
        'parameters': [
            {
                'name': 'adjustment-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/adjustments/{adjustmentId}/cancel-PUT': {
        'parameters': [
            {
                'name': 'adjustmentId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/adjustments-GET': {
        'parameters': [
            {
                'name': 'subscription-number'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/describe/{object}-GET': {
        'parameters': [
            {
                'name': 'object'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'showCurrencyConversionInformation'
            },
        ]
    },
    '/v1/einvoice/templates-POST': {
        'parameters': [
            {
                'name': 'content'
            },
            {
                'name': 'country'
            },
            {
                'name': 'documentType'
            },
            {
                'name': 'name'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/business-regions-POST': {
        'parameters': [
            {
                'name': 'addressLine1'
            },
            {
                'name': 'addressLine2'
            },
            {
                'name': 'businessName'
            },
            {
                'name': 'businessNumber'
            },
            {
                'name': 'businessNumberSchemaId'
            },
            {
                'name': 'city'
            },
            {
                'name': 'contactName'
            },
            {
                'name': 'country'
            },
            {
                'name': 'digitalSignatureEnable'
            },
            {
                'name': 'digitalSignatureBoxEnable'
            },
            {
                'name': 'digitalSignatureBoxPosX'
            },
            {
                'name': 'digitalSignatureBoxPosY'
            },
            {
                'name': 'email'
            },
            {
                'name': 'endpointId'
            },
            {
                'name': 'endpointSchemeId'
            },
            {
                'name': 'phoneNumber'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'serviceProviderId'
            },
            {
                'name': 'state'
            },
            {
                'name': 'taxRegisterNumber'
            },
            {
                'name': 'tradeName'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/templates/{key}-GET': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/templates/{key}-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'content'
            },
            {
                'name': 'country'
            },
            {
                'name': 'documentType'
            },
            {
                'name': 'name'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/templates/{key}-DELETE': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/templates-GET': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'documentType'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/business-regions/{key}-GET': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/business-regions/{key}-DELETE': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/business-regions-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/service-providers-POST': {
        'parameters': [
            {
                'name': 'companyIdentifier'
            },
            {
                'name': 'name'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'test'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/service-providers/{key}-GET': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/service-providers/{key}-DELETE': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/service-providers-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/business-regions/{key}-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'addressLine1'
            },
            {
                'name': 'addressLine2'
            },
            {
                'name': 'businessName'
            },
            {
                'name': 'businessNumber'
            },
            {
                'name': 'businessNumberSchemaId'
            },
            {
                'name': 'city'
            },
            {
                'name': 'contactName'
            },
            {
                'name': 'country'
            },
            {
                'name': 'digitalSignatureEnable'
            },
            {
                'name': 'digitalSignatureBoxEnable'
            },
            {
                'name': 'digitalSignatureBoxPosX'
            },
            {
                'name': 'digitalSignatureBoxPosY'
            },
            {
                'name': 'email'
            },
            {
                'name': 'endpointId'
            },
            {
                'name': 'endpointSchemeId'
            },
            {
                'name': 'phoneNumber'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'serviceProviderId'
            },
            {
                'name': 'state'
            },
            {
                'name': 'taxRegisterNumber'
            },
            {
                'name': 'tradeName'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/einvoice/service-providers/{key}-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'companyIdentifier'
            },
            {
                'name': 'name'
            },
            {
                'name': 'test'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/system-health/payments/volume-summary-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'startTime'
            },
            {
                'name': 'endTime'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'paymentGatewayType'
            },
            {
                'name': 'paymentMethodType'
            },
        ]
    },
    '/v1/files/{file-id}-GET': {
        'parameters': [
            {
                'name': 'file-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/fulfillments-POST': {
        'parameters': [
            {
                'name': 'fulfillments'
            },
            {
                'name': 'processingOptions'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/fulfillments/{key}-GET': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'fulfillment-items'
            },
        ]
    },
    '/v1/fulfillments/{key}-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'description'
            },
            {
                'name': 'billTargetDate'
            },
            {
                'name': 'carrier'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'excludeItemBillingFromRevenueAccounting'
            },
            {
                'name': 'excludeItemBookingFromRevenueAccounting'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'fulfillmentDate'
            },
            {
                'name': 'fulfillmentLocation'
            },
            {
                'name': 'fulfillmentSystem'
            },
            {
                'name': 'fulfillmentType'
            },
            {
                'name': 'orderLineItemId'
            },
            {
                'name': 'quantity'
            },
            {
                'name': 'state'
            },
            {
                'name': 'trackingNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/fulfillments/{key}-DELETE': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/fulfillment-items-POST': {
        'parameters': [
            {
                'name': 'fulfillmentItems'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/fulfillment-items/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/fulfillment-items/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'itemIdentifier'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/fulfillment-items/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/hostedpages-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'versionNumber'
            },
        ]
    },
    '/v1/object/import/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/object/import-POST': {
        'parameters': [
            {
                'name': 'File'
            },
            {
                'name': 'ImportType'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/invoice-schedules-POST': {
        'parameters': [
            {
                'name': 'accountKey'
            },
            {
                'name': 'additionalSubscriptionsToBill'
            },
            {
                'name': 'invoiceSeparately'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'orders'
            },
            {
                'name': 'scheduleItems'
            },
            {
                'name': 'specificSubscriptions'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoice-schedules/{scheduleKey}/execute-POST': {
        'parameters': [
            {
                'name': 'scheduleKey'
            },
            {
                'name': 'scheduleItemId'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoice-schedules/{scheduleKey}-GET': {
        'parameters': [
            {
                'name': 'scheduleKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/invoice-schedules/{scheduleKey}-DELETE': {
        'parameters': [
            {
                'name': 'scheduleKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoice-schedules/{scheduleKey}/pause-PUT': {
        'parameters': [
            {
                'name': 'scheduleKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoice-schedules/{scheduleKey}/resume-PUT': {
        'parameters': [
            {
                'name': 'scheduleKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoice-schedules/{scheduleKey}-PUT': {
        'parameters': [
            {
                'name': 'scheduleKey'
            },
            {
                'name': 'additionalSubscriptionsToBill'
            },
            {
                'name': 'invoiceSeparately'
            },
            {
                'name': 'nextRunDate'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'orders'
            },
            {
                'name': 'scheduleItems'
            },
            {
                'name': 'specificSubscriptions'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices-PUT': {
        'parameters': [
            {
                'name': 'invoices'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/taxationitems-POST': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'taxationItems'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}-DELETE': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/emails-POST': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'emailAddresses'
            },
            {
                'name': 'includeAdditionalEmailAddresses'
            },
            {
                'name': 'useEmailTemplateSetting'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/einvoice/generate-PUT': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}-GET': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/pdf-status-GET': {
        'parameters': [
            {
                'name': 'invoiceKeys'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/application-parts-GET': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/files-GET': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/items-GET': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/invoices/bulk-post-POST': {
        'parameters': [
            {
                'name': 'invoices'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/reverse-PUT': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'applyEffectiveDate'
            },
            {
                'name': 'memoDate'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices-POST': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'autoPay'
            },
            {
                'name': 'billToContact'
            },
            {
                'name': 'billToContactId'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'customRates'
            },
            {
                'name': 'dueDate'
            },
            {
                'name': 'invoiceDate'
            },
            {
                'name': 'invoiceItems'
            },
            {
                'name': 'invoiceNumber'
            },
            {
                'name': 'paymentTerm'
            },
            {
                'name': 'sequenceSet'
            },
            {
                'name': 'soldToContact'
            },
            {
                'name': 'soldToContactId'
            },
            {
                'name': 'soldToSameAsBillTo'
            },
            {
                'name': 'status'
            },
            {
                'name': 'templateId'
            },
            {
                'name': 'transferredToAccounting'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/batch-POST': {
        'parameters': [
            {
                'name': 'invoices'
            },
            {
                'name': 'useSingleTransaction'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/items/{itemId}/taxation-items-GET': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'itemId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}-PUT': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'autoPay'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'dueDate'
            },
            {
                'name': 'invoiceDate'
            },
            {
                'name': 'invoiceItems'
            },
            {
                'name': 'transferredToAccounting'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/files-POST': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/v1/invoices/{invoiceKey}/write-off-PUT': {
        'parameters': [
            {
                'name': 'invoiceKey'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'items'
            },
            {
                'name': 'memoDate'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Transaction__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/journal-runs-POST': {
        'parameters': [
            {
                'name': 'journalEntryDate'
            },
            {
                'name': 'transactionTypes'
            },
            {
                'name': 'accountingPeriodName'
            },
            {
                'name': 'organizationLabels'
            },
            {
                'name': 'targetEndDate'
            },
            {
                'name': 'targetStartDate'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/journal-runs/{jr-number}-GET': {
        'parameters': [
            {
                'name': 'jr-number'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/journal-runs/{jr-number}-DELETE': {
        'parameters': [
            {
                'name': 'jr-number'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/journal-runs/{jr-number}/cancel-PUT': {
        'parameters': [
            {
                'name': 'jr-number'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/bulk-POST': {
        'parameters': [
            {
                'name': 'file'
            },
            {
                'name': 'params'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/bulk/{bulk-key}-GET': {
        'parameters': [
            {
                'name': 'bulk-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/bulk/{bulk-key}/stop-PUT': {
        'parameters': [
            {
                'name': 'bulk-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/deployment-manager/deployments/tenant/product_catalog-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sendEmail'
            },
            {
                'name': 'inActiveProducts'
            },
            {
                'name': 'activeProducts'
            },
            {
                'name': 'activeRatePlans'
            },
            {
                'name': 'inActiveRatePlans'
            },
            {
                'name': 'compareField'
            },
            {
                'name': 'sourceTenantId'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'emails'
            },
            {
                'name': 'comments'
            },
        ]
    },
    '/deployment-manager/deployments/templates-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sendEmail'
            },
            {
                'name': 'template'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'emails'
            },
            {
                'name': 'comments'
            },
        ]
    },
    '/deployment-manager/deployments/tenants-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sendEmail'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'notifications'
            },
            {
                'name': 'workflows'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'productCatalog'
            },
            {
                'name': 'userRoles'
            },
            {
                'name': 'reporting'
            },
            {
                'name': 'sourceTenantId'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'emails'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'customObjects'
            },
            {
                'name': 'taxation'
            },
        ]
    },
    '/deployment-manager/deployments/template/product_catalog-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sendEmail'
            },
            {
                'name': 'template'
            },
            {
                'name': 'inActiveProducts'
            },
            {
                'name': 'activeProducts'
            },
            {
                'name': 'activeRatePlans'
            },
            {
                'name': 'inActiveRatePlans'
            },
            {
                'name': 'compareField'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'emails'
            },
            {
                'name': 'comments'
            },
        ]
    },
    '/deployment-manager/deployments/{migrationId}-GET': {
        'parameters': [
            {
                'name': 'migrationId'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/deployment-manager/deployments/{migrationId}/revert-POST': {
        'parameters': [
            {
                'name': 'migrationId'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/notification-history/callout-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'endTime'
            },
            {
                'name': 'startTime'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'failedOnly'
            },
            {
                'name': 'eventCategory'
            },
            {
                'name': 'includeResponseContent'
            },
        ]
    },
    '/notifications/email-templates-POST': {
        'parameters': [
            {
                'name': 'emailBody'
            },
            {
                'name': 'emailSubject'
            },
            {
                'name': 'fromEmailType'
            },
            {
                'name': 'name'
            },
            {
                'name': 'toEmailType'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'bccEmailAddress'
            },
            {
                'name': 'ccEmailAddress'
            },
            {
                'name': 'ccEmailType'
            },
            {
                'name': 'encodingType'
            },
            {
                'name': 'eventCategory'
            },
            {
                'name': 'eventTypeName'
            },
            {
                'name': 'eventTypeNamespace'
            },
            {
                'name': 'fromEmailAddress'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'isHtml'
            },
            {
                'name': 'replyToEmailAddress'
            },
            {
                'name': 'replyToEmailType'
            },
            {
                'name': 'toEmailAddress'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/notification-definitions-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'associatedAccount'
            },
            {
                'name': 'callout'
            },
            {
                'name': 'calloutActive'
            },
            {
                'name': 'communicationProfileId'
            },
            {
                'name': 'emailActive'
            },
            {
                'name': 'emailTemplateId'
            },
            {
                'name': 'eventCategory'
            },
            {
                'name': 'eventTypeName'
            },
            {
                'name': 'eventTypeNamespace'
            },
            {
                'name': 'filterRule'
            },
            {
                'name': 'filterRuleParams'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/email-templates/import-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'allowPartialSuccess'
            },
            {
                'name': 'emailTemplates'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/email-templates/{id}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/notification-definitions/{id}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/history-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/notification-history/email-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'endTime'
            },
            {
                'name': 'startTime'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'failedOnly'
            },
            {
                'name': 'eventCategory'
            },
        ]
    },
    '/notifications/email-templates/{id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/notification-definitions/{id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/history/tasks/{id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/email-templates-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'eventCategory'
            },
            {
                'name': 'eventTypeName'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/notifications/notification-definitions-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'profileId'
            },
            {
                'name': 'eventCategory'
            },
            {
                'name': 'eventTypeName'
            },
            {
                'name': 'emailTemplateId'
            },
        ]
    },
    '/notifications/callout-histories/resend-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/email-histories/resend-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/email-templates/{id}-PUT': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'bccEmailAddress'
            },
            {
                'name': 'ccEmailAddress'
            },
            {
                'name': 'ccEmailType'
            },
            {
                'name': 'emailBody'
            },
            {
                'name': 'emailSubject'
            },
            {
                'name': 'encodingType'
            },
            {
                'name': 'fromEmailAddress'
            },
            {
                'name': 'fromEmailType'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'isHtml'
            },
            {
                'name': 'name'
            },
            {
                'name': 'replyToEmailAddress'
            },
            {
                'name': 'replyToEmailType'
            },
            {
                'name': 'toEmailAddress'
            },
            {
                'name': 'toEmailType'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/notifications/notification-definitions/{id}-PUT': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'associatedAccount'
            },
            {
                'name': 'callout'
            },
            {
                'name': 'calloutActive'
            },
            {
                'name': 'communicationProfileId'
            },
            {
                'name': 'emailActive'
            },
            {
                'name': 'emailTemplateId'
            },
            {
                'name': 'filterRule'
            },
            {
                'name': 'filterRuleParams'
            },
            {
                'name': 'name'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/oauth/token-POST': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/operations/billing-preview-POST': {
        'parameters': [
            {
                'name': 'targetDate'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'assumeRenewal'
            },
            {
                'name': 'chargeTypeToExclude'
            },
            {
                'name': 'includingDraftItems'
            },
            {
                'name': 'includingEvergreenSubscription'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/operations/bulk-pdf-POST': {
        'parameters': [
            {
                'name': 'documents'
            },
            {
                'name': 'fileName'
            },
            {
                'name': 'name'
            },
            {
                'name': 'indexFileFormat'
            },
            {
                'name': 'generateMissingPDF'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/operations/bulk-pdf/{jobId}-GET': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/operations/jobs/{jobId}-GET': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/operations/invoice-collect-POST': {
        'parameters': [
            {
                'name': 'accountKey'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'invoiceDate'
            },
            {
                'name': 'invoiceId'
            },
            {
                'name': 'invoiceNumber'
            },
            {
                'name': 'invoiceTargetDate'
            },
            {
                'name': 'paymentGateway'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/orderActions/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'orderAction'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/order-line-items/{itemId}-GET': {
        'parameters': [
            {
                'name': 'itemId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'fulfillment'
            },
        ]
    },
    '/v1/order-line-items/{itemId}-PUT': {
        'parameters': [
            {
                'name': 'itemId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'UOM'
            },
            {
                'name': 'accountingCode'
            },
            {
                'name': 'adjustmentLiabilityAccountingCode'
            },
            {
                'name': 'adjustmentRevenueAccountingCode'
            },
            {
                'name': 'amountPerUnit'
            },
            {
                'name': 'billTargetDate'
            },
            {
                'name': 'billTo'
            },
            {
                'name': 'billingRule'
            },
            {
                'name': 'contractAssetAccountingCode'
            },
            {
                'name': 'contractLiabilityAccountingCode'
            },
            {
                'name': 'contractRecognizedRevenueAccountingCode'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'deferredRevenueAccountingCode'
            },
            {
                'name': 'excludeItemBillingFromRevenueAccounting'
            },
            {
                'name': 'excludeItemBookingFromRevenueAccounting'
            },
            {
                'name': 'invoiceGroupNumber'
            },
            {
                'name': 'inlineDiscountPerUnit'
            },
            {
                'name': 'inlineDiscountType'
            },
            {
                'name': 'isAllocationEligible'
            },
            {
                'name': 'isUnbilled'
            },
            {
                'name': 'itemName'
            },
            {
                'name': 'itemNumber'
            },
            {
                'name': 'itemState'
            },
            {
                'name': 'itemType'
            },
            {
                'name': 'listPricePerUnit'
            },
            {
                'name': 'ownerAccountNumber'
            },
            {
                'name': 'productCode'
            },
            {
                'name': 'purchaseOrderNumber'
            },
            {
                'name': 'quantity'
            },
            {
                'name': 'recognizedRevenueAccountingCode'
            },
            {
                'name': 'relatedSubscriptionNumber'
            },
            {
                'name': 'revenueRecognitionRule'
            },
            {
                'name': 'revenueRecognitionTiming'
            },
            {
                'name': 'revenueAmortizationMethod'
            },
            {
                'name': 'sequenceSetId'
            },
            {
                'name': 'soldTo'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'taxMode'
            },
            {
                'name': 'transactionEndDate'
            },
            {
                'name': 'transactionStartDate'
            },
            {
                'name': 'unbilledReceivablesAccountingCode'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/order-line-items/bulk-POST': {
        'parameters': [
            {
                'name': 'orderLineItems'
            },
            {
                'name': 'processingOptions'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'dateFilterOption'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/async/orders-POST': {
        'parameters': [
            {
                'name': 'orderDate'
            },
            {
                'name': 'description'
            },
            {
                'name': 'category'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'existingAccountNumber'
            },
            {
                'name': 'externallyManagedBy'
            },
            {
                'name': 'newAccount'
            },
            {
                'name': 'orderLineItems'
            },
            {
                'name': 'orderNumber'
            },
            {
                'name': 'processingOptions'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'returnIds'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/async-jobs/{jobId}-GET': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/orders-POST': {
        'parameters': [
            {
                'name': 'orderDate'
            },
            {
                'name': 'description'
            },
            {
                'name': 'category'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'existingAccountNumber'
            },
            {
                'name': 'externallyManagedBy'
            },
            {
                'name': 'newAccount'
            },
            {
                'name': 'orderLineItems'
            },
            {
                'name': 'orderNumber'
            },
            {
                'name': 'processingOptions'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'schedulingOptions'
            },
            {
                'name': 'status'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'returnIds'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/orders/{orderNumber}-GET': {
        'parameters': [
            {
                'name': 'orderNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders/{orderNumber}-PUT': {
        'parameters': [
            {
                'name': 'orderDate'
            },
            {
                'name': 'orderNumber'
            },
            {
                'name': 'description'
            },
            {
                'name': 'category'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'existingAccountNumber'
            },
            {
                'name': 'externallyManagedBy'
            },
            {
                'name': 'orderLineItems'
            },
            {
                'name': 'orderNumber'
            },
            {
                'name': 'processingOptions'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'schedulingOptions'
            },
            {
                'name': 'status'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders/{orderNumber}-DELETE': {
        'parameters': [
            {
                'name': 'orderNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders/{orderNumber}/activate-PUT': {
        'parameters': [
            {
                'name': 'orderNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders/{orderNumber}/cancel-PUT': {
        'parameters': [
            {
                'name': 'orderNumber'
            },
            {
                'name': 'cancelReason'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders/{orderNumber}/triggerDates-PUT': {
        'parameters': [
            {
                'name': 'orderNumber'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders/invoiceOwner/{accountNumber}-GET': {
        'parameters': [
            {
                'name': 'accountNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'dateFilterOption'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/orders/subscription/{subscriptionNumber}-GET': {
        'parameters': [
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'dateFilterOption'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/orders/subscriptionOwner/{accountNumber}-GET': {
        'parameters': [
            {
                'name': 'accountNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'dateFilterOption'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
        ]
    },
    '/v1/orders/subscription/{subscription-key}/pending-GET': {
        'parameters': [
            {
                'name': 'subscription-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders/preview-POST': {
        'parameters': [
            {
                'name': 'orderDate'
            },
            {
                'name': 'previewOptions'
            },
            {
                'name': 'description'
            },
            {
                'name': 'category'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'existingAccountNumber'
            },
            {
                'name': 'orderLineItems'
            },
            {
                'name': 'orderNumber'
            },
            {
                'name': 'previewAccountInfo'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/async/orders/preview-POST': {
        'parameters': [
            {
                'name': 'orderDate'
            },
            {
                'name': 'previewOptions'
            },
            {
                'name': 'description'
            },
            {
                'name': 'category'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'existingAccountNumber'
            },
            {
                'name': 'orderLineItems'
            },
            {
                'name': 'orderNumber'
            },
            {
                'name': 'previewAccountInfo'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders/{orderNumber}/customFields-PUT': {
        'parameters': [
            {
                'name': 'orderNumber'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/subscriptions/{subscriptionNumber}/customFields-PUT': {
        'parameters': [
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'ratePlans'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}/voidAuthorize-POST': {
        'parameters': [
            {
                'name': 'gatewayOrderId'
            },
            {
                'name': 'transactionId'
            },
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'gatewayOptions'
            },
            {
                'name': 'paymentGatewayId'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}/authorize-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'gatewayOrderId'
            },
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'gatewayOptions'
            },
            {
                'name': 'mitTransactionSource'
            },
            {
                'name': 'paymentGatewayId'
            },
            {
                'name': 'softDescriptor'
            },
            {
                'name': 'softDescriptorPhone'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/refunds/{refund-key}/reconcile-POST': {
        'parameters': [
            {
                'name': 'refund-key'
            },
            {
                'name': 'action'
            },
            {
                'name': 'actionDate'
            },
            {
                'name': 'gatewayReconciliationReason'
            },
            {
                'name': 'gatewayReconciliationStatus'
            },
            {
                'name': 'payoutId'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/gateway-settlement/payments/{payment-key}/reject-POST': {
        'parameters': [
            {
                'name': 'payment-key'
            },
            {
                'name': 'gatewayReconciliationReason'
            },
            {
                'name': 'gatewayReconciliationStatus'
            },
            {
                'name': 'gatewayResponse'
            },
            {
                'name': 'gatewayResponseCode'
            },
            {
                'name': 'referenceId'
            },
            {
                'name': 'secondReferenceId'
            },
            {
                'name': 'settledOn'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/gateway-settlement/payments/{payment-key}/chargeback-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'payment-key'
            },
            {
                'name': 'gatewayReconciliationReason'
            },
            {
                'name': 'gatewayReconciliationStatus'
            },
            {
                'name': 'gatewayResponse'
            },
            {
                'name': 'gatewayResponseCode'
            },
            {
                'name': 'payoutId'
            },
            {
                'name': 'referenceId'
            },
            {
                'name': 'secondReferenceId'
            },
            {
                'name': 'settledOn'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/gateway-settlement/payments/{payment-key}/settle-POST': {
        'parameters': [
            {
                'name': 'payment-key'
            },
            {
                'name': 'gatewayReconciliationReason'
            },
            {
                'name': 'gatewayReconciliationStatus'
            },
            {
                'name': 'payoutId'
            },
            {
                'name': 'settledOn'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/paymentgateways-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/object/payment-method-snapshot/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/object/payment-method-transaction-log/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/payment-method-updaters/batches-POST': {
        'parameters': [
            {
                'name': 'billingCycleDay'
            },
            {
                'name': 'updaterAccountId'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-method-updaters-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}/profiles/{profile-number}/cancel-POST': {
        'parameters': [
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'profile-number'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/web-payments/sessions-POST': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'paymentGateway'
            },
            {
                'name': 'processPayment'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'authAmount'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}/profiles-POST': {
        'parameters': [
            {
                'name': 'consentAgreementSrc'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'action'
            },
            {
                'name': 'agreedOn'
            },
            {
                'name': 'authGateway'
            },
            {
                'name': 'cardSecurityCode'
            },
            {
                'name': 'consentAgreementRef'
            },
            {
                'name': 'networkTransactionId'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}/profiles/{profile-number}/expire-POST': {
        'parameters': [
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'profile-number'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/payment-methods/apple-pay/domains-GET': {
        'parameters': [
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'domainName'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}-GET': {
        'parameters': [
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}-PUT': {
        'parameters': [
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'accountHolderInfo'
            },
            {
                'name': 'accountKey'
            },
            {
                'name': 'authGateway'
            },
            {
                'name': 'currencyCode'
            },
            {
                'name': 'gatewayOptions'
            },
            {
                'name': 'ipAddress'
            },
            {
                'name': 'mandateInfo'
            },
            {
                'name': 'processingOptions'
            },
            {
                'name': 'expirationMonth'
            },
            {
                'name': 'expirationYear'
            },
            {
                'name': 'securityCode'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'cardHolderInfo'
            },
            {
                'name': 'cardNumber'
            },
            {
                'name': 'cardType'
            },
            {
                'name': 'checkDuplicated'
            },
            {
                'name': 'expirationMonth'
            },
            {
                'name': 'expirationYear'
            },
            {
                'name': 'identityNumber'
            },
            {
                'name': 'mitConsentAgreementRef'
            },
            {
                'name': 'mitConsentAgreementSrc'
            },
            {
                'name': 'mitNetworkTransactionId'
            },
            {
                'name': 'mitProfileAction'
            },
            {
                'name': 'mitProfileAgreedOn'
            },
            {
                'name': 'mitProfileType'
            },
            {
                'name': 'screeningAmount'
            },
            {
                'name': 'securityCode'
            },
            {
                'name': 'mandateInfo'
            },
            {
                'name': 'processingOptions'
            },
            {
                'name': 'accountKey'
            },
            {
                'name': 'authGateway'
            },
            {
                'name': 'currencyCode'
            },
            {
                'name': 'gatewayOptions'
            },
            {
                'name': 'ipAddress'
            },
            {
                'name': 'makeDefault'
            },
            {
                'name': 'skipValidation'
            },
            {
                'name': 'creditCardMaskNumber'
            },
            {
                'name': 'secondTokenId'
            },
            {
                'name': 'tokenId'
            },
            {
                'name': 'addressLine1'
            },
            {
                'name': 'addressLine2'
            },
            {
                'name': 'bankABACode'
            },
            {
                'name': 'bankAccountName'
            },
            {
                'name': 'bankAccountNumber'
            },
            {
                'name': 'bankAccountType'
            },
            {
                'name': 'bankName'
            },
            {
                'name': 'city'
            },
            {
                'name': 'country'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zipCode'
            },
            {
                'name': 'IBAN'
            },
            {
                'name': 'accountHolderInfo'
            },
            {
                'name': 'accountMaskNumber'
            },
            {
                'name': 'businessIdentificationCode'
            },
            {
                'name': 'tokenize'
            },
            {
                'name': 'tokens'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'bankCode'
            },
            {
                'name': 'branchCode'
            },
            {
                'name': 'BAID'
            },
            {
                'name': 'email'
            },
            {
                'name': 'preapprovalKey'
            },
            {
                'name': 'applePaymentData'
            },
            {
                'name': 'googlePaymentToken'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}-DELETE': {
        'parameters': [
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/decryption-POST': {
        'parameters': [
            {
                'name': 'integrationType'
            },
            {
                'name': 'merchantID'
            },
            {
                'name': 'paymentToken'
            },
            {
                'name': 'accountID'
            },
            {
                'name': 'cardHolderInfo'
            },
            {
                'name': 'invoiceId'
            },
            {
                'name': 'mitConsentAgreementSrc'
            },
            {
                'name': 'mitProfileAction'
            },
            {
                'name': 'mitProfileType'
            },
            {
                'name': 'paymentGateway'
            },
            {
                'name': 'processPayment'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/payment-methods/apple-pay/domains-POST': {
        'parameters': [
            {
                'name': 'domainName'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}/scrub-PUT': {
        'parameters': [
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}/profiles-GET': {
        'parameters': [
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'includeAll'
            },
        ]
    },
    '/payment-methods/apple-pay/domains/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-methods/{payment-method-id}/verify-PUT': {
        'parameters': [
            {
                'name': 'payment-method-id'
            },
            {
                'name': 'currencyCode'
            },
            {
                'name': 'gatewayOptions'
            },
            {
                'name': 'paymentGatewayName'
            },
            {
                'name': 'securityCode'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/payment-runs-POST': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'applyCreditBalance'
            },
            {
                'name': 'autoApplyCreditMemo'
            },
            {
                'name': 'autoApplyUnappliedPayment'
            },
            {
                'name': 'batch'
            },
            {
                'name': 'billCycleDay'
            },
            {
                'name': 'billingRunId'
            },
            {
                'name': 'collectPayment'
            },
            {
                'name': 'consolidatedPayment'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'data'
            },
            {
                'name': 'organizationLabels'
            },
            {
                'name': 'paymentGatewayId'
            },
            {
                'name': 'processPaymentWithClosedPM'
            },
            {
                'name': 'runDate'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-runs/{paymentRunKey}-GET': {
        'parameters': [
            {
                'name': 'paymentRunKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-runs/{paymentRunKey}-PUT': {
        'parameters': [
            {
                'name': 'paymentRunKey'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'applyCreditBalance'
            },
            {
                'name': 'autoApplyCreditMemo'
            },
            {
                'name': 'autoApplyUnappliedPayment'
            },
            {
                'name': 'batch'
            },
            {
                'name': 'billCycleDay'
            },
            {
                'name': 'billingRunId'
            },
            {
                'name': 'collectPayment'
            },
            {
                'name': 'consolidatedPayment'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'organizationLabels'
            },
            {
                'name': 'paymentGatewayId'
            },
            {
                'name': 'processPaymentWithClosedPM'
            },
            {
                'name': 'runDate'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-runs/{paymentRunKey}-DELETE': {
        'parameters': [
            {
                'name': 'paymentRunKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/payment-runs/{paymentRunKey}/data-GET': {
        'parameters': [
            {
                'name': 'paymentRunKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/payment-runs/{paymentRunKey}/summary-GET': {
        'parameters': [
            {
                'name': 'paymentRunKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/payment-runs-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'createdById'
            },
            {
                'name': 'createdDate'
            },
            {
                'name': 'status'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'updatedById'
            },
            {
                'name': 'updatedDate'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/payment-schedules/{paymentScheduleKey}/items-POST': {
        'parameters': [
            {
                'name': 'paymentScheduleKey'
            },
            {
                'name': 'items'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedules/{paymentScheduleKey}/cancel-PUT': {
        'parameters': [
            {
                'name': 'cancelDate'
            },
            {
                'name': 'paymentScheduleKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedule-items/{item-id}/cancel-PUT': {
        'parameters': [
            {
                'name': 'item-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedules-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'billingDocument'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'items'
            },
            {
                'name': 'occurrences'
            },
            {
                'name': 'paymentGatewayId'
            },
            {
                'name': 'paymentMethodId'
            },
            {
                'name': 'paymentOption'
            },
            {
                'name': 'paymentScheduleNumber'
            },
            {
                'name': 'period'
            },
            {
                'name': 'prepayment'
            },
            {
                'name': 'runHour'
            },
            {
                'name': 'standalone'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'totalAmount'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedules/{paymentScheduleKey}-GET': {
        'parameters': [
            {
                'name': 'paymentScheduleKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'nextPendingItems'
            },
            {
                'name': 'lastProcessedItems'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedules/{paymentScheduleKey}-PUT': {
        'parameters': [
            {
                'name': 'paymentScheduleKey'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'occurrences'
            },
            {
                'name': 'paymentGatewayId'
            },
            {
                'name': 'paymentMethodId'
            },
            {
                'name': 'paymentOption'
            },
            {
                'name': 'period'
            },
            {
                'name': 'periodStartDate'
            },
            {
                'name': 'runHour'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedule-items/{item-id}-GET': {
        'parameters': [
            {
                'name': 'item-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedule-items/{item-id}-PUT': {
        'parameters': [
            {
                'name': 'item-id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'linkPayments'
            },
            {
                'name': 'paymentGatewayId'
            },
            {
                'name': 'paymentId'
            },
            {
                'name': 'paymentMethodId'
            },
            {
                'name': 'paymentOption'
            },
            {
                'name': 'runHour'
            },
            {
                'name': 'scheduledDate'
            },
            {
                'name': 'unlinkPayments'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedules/statistics/{yyyy-mm-dd}-GET': {
        'parameters': [
            {
                'name': 'yyyy-mm-dd'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payment-schedules/{paymentScheduleKey}/preview-PUT': {
        'parameters': [
            {
                'name': 'paymentScheduleKey'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'occurrences'
            },
            {
                'name': 'paymentGatewayId'
            },
            {
                'name': 'paymentMethodId'
            },
            {
                'name': 'paymentOption'
            },
            {
                'name': 'period'
            },
            {
                'name': 'periodStartDate'
            },
            {
                'name': 'runHour'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedules-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'lastProcessedItems'
            },
            {
                'name': 'nextPendingItems'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedules/batch-POST': {
        'parameters': [
            {
                'name': 'paymentSchedules'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedule-items/retry-payment-POST': {
        'parameters': [
            {
                'name': 'items'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/payment-schedule-items/{item-id}/skip-PUT': {
        'parameters': [
            {
                'name': 'item-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/object/payment-transaction-log/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/payments/{paymentKey}/apply-PUT': {
        'parameters': [
            {
                'name': 'paymentKey'
            },
            {
                'name': 'debitMemos'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'invoices'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments/{paymentKey}/cancel-PUT': {
        'parameters': [
            {
                'name': 'paymentKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments-POST': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'authTransactionId'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'customRates'
            },
            {
                'name': 'debitMemos'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'financeInformation'
            },
            {
                'name': 'gatewayId'
            },
            {
                'name': 'gatewayOptions'
            },
            {
                'name': 'gatewayOrderId'
            },
            {
                'name': 'invoices'
            },
            {
                'name': 'mitTransactionSource'
            },
            {
                'name': 'paymentGatewayNumber'
            },
            {
                'name': 'paymentMethodId'
            },
            {
                'name': 'paymentMethodType'
            },
            {
                'name': 'paymentOption'
            },
            {
                'name': 'paymentScheduleKey'
            },
            {
                'name': 'prepayment'
            },
            {
                'name': 'referenceId'
            },
            {
                'name': 'softDescriptor'
            },
            {
                'name': 'softDescriptorPhone'
            },
            {
                'name': 'standalone'
            },
            {
                'name': 'type'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Transaction__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments/{paymentKey}-GET': {
        'parameters': [
            {
                'name': 'paymentKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments/{paymentKey}-DELETE': {
        'parameters': [
            {
                'name': 'paymentKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments/{paymentKey}/parts/{partid}/itemparts/{itempartid}-GET': {
        'parameters': [
            {
                'name': 'partid'
            },
            {
                'name': 'itempartid'
            },
            {
                'name': 'paymentKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments/{paymentKey}/parts/{partid}/itemparts-GET': {
        'parameters': [
            {
                'name': 'partid'
            },
            {
                'name': 'paymentKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/payments/{paymentKey}/parts/{partid}-GET': {
        'parameters': [
            {
                'name': 'partid'
            },
            {
                'name': 'paymentKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments/{paymentKey}/parts-GET': {
        'parameters': [
            {
                'name': 'paymentKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/payments/{paymentKey}/refunds-POST': {
        'parameters': [
            {
                'name': 'paymentKey'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'customRates'
            },
            {
                'name': 'financeInformation'
            },
            {
                'name': 'gatewayOptions'
            },
            {
                'name': 'methodType'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'referenceId'
            },
            {
                'name': 'refundDate'
            },
            {
                'name': 'secondRefundReferenceId'
            },
            {
                'name': 'softDescriptor'
            },
            {
                'name': 'softDescriptorPhone'
            },
            {
                'name': 'totalAmount'
            },
            {
                'name': 'type'
            },
            {
                'name': 'refundTransactionType'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'SynctoNetSuite__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments/{paymentKey}/refunds/unapply-POST': {
        'parameters': [
            {
                'name': 'paymentKey'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'debitMemos'
            },
            {
                'name': 'financeInformation'
            },
            {
                'name': 'gatewayOptions'
            },
            {
                'name': 'invoices'
            },
            {
                'name': 'methodType'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'referenceId'
            },
            {
                'name': 'refundDate'
            },
            {
                'name': 'secondRefundReferenceId'
            },
            {
                'name': 'softDescriptor'
            },
            {
                'name': 'softDescriptorPhone'
            },
            {
                'name': 'totalAmount'
            },
            {
                'name': 'type'
            },
            {
                'name': 'refundTransactionType'
            },
            {
                'name': 'writeOff'
            },
            {
                'name': 'writeOffOptions'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'SynctoNetSuite__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'appliedAmount'
            },
            {
                'name': 'createdById'
            },
            {
                'name': 'createdDate'
            },
            {
                'name': 'creditBalanceAmount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'number'
            },
            {
                'name': 'refundAmount'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'unappliedAmount'
            },
            {
                'name': 'updatedById'
            },
            {
                'name': 'updatedDate'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/payments/{paymentKey}/transfer-PUT': {
        'parameters': [
            {
                'name': 'paymentKey'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments/{paymentKey}/unapply-PUT': {
        'parameters': [
            {
                'name': 'paymentKey'
            },
            {
                'name': 'debitMemos'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'invoices'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/payments/{paymentId}-PUT': {
        'parameters': [
            {
                'name': 'paymentId'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'financeInformation'
            },
            {
                'name': 'gatewayState'
            },
            {
                'name': 'paymentScheduleKey'
            },
            {
                'name': 'referenceId'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Transaction__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/prepaid-balance-funds/deplete-POST': {
        'parameters': [
            {
                'name': 'fundIds'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/ppdd/reverse-rollover-POST': {
        'parameters': [
            {
                'name': 'destinationValidityPeriod'
            },
            {
                'name': 'prepaymentUom'
            },
            {
                'name': 'sourceValidityPeriod'
            },
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/ppdd/rollover-POST': {
        'parameters': [
            {
                'name': 'destinationValidityPeriod'
            },
            {
                'name': 'prepaymentUom'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'sourceValidityPeriod'
            },
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/product-charge-definitions-POST': {
        'parameters': [
            {
                'name': 'billingPeriod'
            },
            {
                'name': 'billingTiming'
            },
            {
                'name': 'chargeModel'
            },
            {
                'name': 'defaultQuantity'
            },
            {
                'name': 'effectiveEndDate'
            },
            {
                'name': 'effectiveStartDate'
            },
            {
                'name': 'listPriceBase'
            },
            {
                'name': 'prices'
            },
            {
                'name': 'productRatePlanChargeId'
            },
            {
                'name': 'productRatePlanChargeNumber'
            },
            {
                'name': 'productRatePlanId'
            },
            {
                'name': 'productRatePlanNumber'
            },
            {
                'name': 'specificBillingPeriod'
            },
            {
                'name': 'specificListPriceBase'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'taxMode'
            },
            {
                'name': 'taxable'
            },
            {
                'name': 'term'
            },
            {
                'name': 'termPeriodType'
            },
            {
                'name': 'termType'
            },
            {
                'name': 'uom'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/product-charge-definitions/bulk-POST': {
        'parameters': [
            {
                'name': 'productChargeDefinitions'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/product-charge-definitions/{product-charge-definition-key}-DELETE': {
        'parameters': [
            {
                'name': 'product-charge-definition-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/product-charge-definitions/{product-charge-definition-key}-GET': {
        'parameters': [
            {
                'name': 'product-charge-definition-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'hide-inherited-values'
            },
        ]
    },
    '/v1/product-charge-definitions-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'charge'
            },
            {
                'name': 'rateplan'
            },
            {
                'name': 'hide-inherited-values'
            },
        ]
    },
    '/v1/product-charge-definitions/{product-charge-definition-key}-PUT': {
        'parameters': [
            {
                'name': 'product-charge-definition-key'
            },
            {
                'name': 'billingPeriod'
            },
            {
                'name': 'billingTiming'
            },
            {
                'name': 'chargeModel'
            },
            {
                'name': 'defaultQuantity'
            },
            {
                'name': 'effectiveEndDate'
            },
            {
                'name': 'effectiveStartDate'
            },
            {
                'name': 'listPriceBase'
            },
            {
                'name': 'prices'
            },
            {
                'name': 'specificBillingPeriod'
            },
            {
                'name': 'specificListPriceBase'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'taxMode'
            },
            {
                'name': 'taxable'
            },
            {
                'name': 'term'
            },
            {
                'name': 'termPeriodType'
            },
            {
                'name': 'termType'
            },
            {
                'name': 'uom'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/product-charge-definitions/bulk-PUT': {
        'parameters': [
            {
                'name': 'productChargeDefinitions'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/object/product-rate-plan-charge-tier/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/object/product-rate-plan-charge-tier/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Price'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/object/product-rate-plan-charge/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/object/product-rate-plan-charge/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/object/product-rate-plan-charge-POST': {
        'parameters': [
            {
                'name': 'AccountingCode'
            },
            {
                'name': 'ApplyDiscountTo'
            },
            {
                'name': 'BillCycleDay'
            },
            {
                'name': 'BillCycleType'
            },
            {
                'name': 'BillingPeriod'
            },
            {
                'name': 'BillingPeriodAlignment'
            },
            {
                'name': 'BillingTiming'
            },
            {
                'name': 'ChargeFunction'
            },
            {
                'name': 'CommitmentType'
            },
            {
                'name': 'ChargeModel'
            },
            {
                'name': 'ChargeModelConfiguration'
            },
            {
                'name': 'ChargeType'
            },
            {
                'name': 'CreditOption'
            },
            {
                'name': 'DefaultQuantity'
            },
            {
                'name': 'DeferredRevenueAccount'
            },
            {
                'name': 'DeliverySchedule'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'DiscountLevel'
            },
            {
                'name': 'DrawdownRate'
            },
            {
                'name': 'DrawdownUom'
            },
            {
                'name': 'EndDateCondition'
            },
            {
                'name': 'ExcludeItemBillingFromRevenueAccounting'
            },
            {
                'name': 'ExcludeItemBookingFromRevenueAccounting'
            },
            {
                'name': 'IncludedUnits'
            },
            {
                'name': 'IsAllocationEligible'
            },
            {
                'name': 'IsPrepaid'
            },
            {
                'name': 'IsRollover'
            },
            {
                'name': 'IsStackedDiscount'
            },
            {
                'name': 'IsUnbilled'
            },
            {
                'name': 'LegacyRevenueReporting'
            },
            {
                'name': 'ListPriceBase'
            },
            {
                'name': 'MaxQuantity'
            },
            {
                'name': 'MinQuantity'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'NumberOfPeriod'
            },
            {
                'name': 'OverageCalculationOption'
            },
            {
                'name': 'OverageUnusedUnitsCreditOption'
            },
            {
                'name': 'PrepaidOperationType'
            },
            {
                'name': 'PrepaidQuantity'
            },
            {
                'name': 'PrepaidTotalQuantity'
            },
            {
                'name': 'PrepaidUom'
            },
            {
                'name': 'PriceChangeOption'
            },
            {
                'name': 'PriceIncreaseOption'
            },
            {
                'name': 'PriceIncreasePercentage'
            },
            {
                'name': 'ProductCategory'
            },
            {
                'name': 'ProductClass'
            },
            {
                'name': 'ProductFamily'
            },
            {
                'name': 'ProductLine'
            },
            {
                'name': 'RevenueRecognitionTiming'
            },
            {
                'name': 'RevenueAmortizationMethod'
            },
            {
                'name': 'ProductRatePlanChargeNumber'
            },
            {
                'name': 'ProductRatePlanChargeTierData'
            },
            {
                'name': 'ProductRatePlanId'
            },
            {
                'name': 'RatingGroup'
            },
            {
                'name': 'RecognizedRevenueAccount'
            },
            {
                'name': 'RevRecCode'
            },
            {
                'name': 'RevRecTriggerCondition'
            },
            {
                'name': 'RevenueRecognitionRuleName'
            },
            {
                'name': 'RolloverApply'
            },
            {
                'name': 'RolloverPeriods'
            },
            {
                'name': 'SmoothingModel'
            },
            {
                'name': 'SpecificBillingPeriod'
            },
            {
                'name': 'SpecificListPriceBase'
            },
            {
                'name': 'TaxCode'
            },
            {
                'name': 'TaxMode'
            },
            {
                'name': 'Taxable'
            },
            {
                'name': 'TriggerEvent'
            },
            {
                'name': 'UOM'
            },
            {
                'name': 'UpToPeriods'
            },
            {
                'name': 'UpToPeriodsType'
            },
            {
                'name': 'UsageRecordRatingOption'
            },
            {
                'name': 'UseDiscountSpecificAccountingCode'
            },
            {
                'name': 'UseTenantDefaultForPriceChange'
            },
            {
                'name': 'ValidityPeriodType'
            },
            {
                'name': 'WeeklyBillCycleDay'
            },
            {
                'name': 'ApplyToBillingPeriodPartially'
            },
            {
                'name': 'RolloverPeriodLength'
            },
            {
                'name': 'Formula'
            },
            {
                'name': 'Class__NS'
            },
            {
                'name': 'DeferredRevAccount__NS'
            },
            {
                'name': 'Department__NS'
            },
            {
                'name': 'IncludeChildren__NS'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'ItemType__NS'
            },
            {
                'name': 'Location__NS'
            },
            {
                'name': 'RecognizedRevAccount__NS'
            },
            {
                'name': 'RevRecEnd__NS'
            },
            {
                'name': 'RevRecStart__NS'
            },
            {
                'name': 'RevRecTemplateType__NS'
            },
            {
                'name': 'Subsidiary__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/object/product-rate-plan-charge/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'AccountingCode'
            },
            {
                'name': 'ApplyDiscountTo'
            },
            {
                'name': 'BillCycleDay'
            },
            {
                'name': 'BillCycleType'
            },
            {
                'name': 'BillingPeriod'
            },
            {
                'name': 'BillingPeriodAlignment'
            },
            {
                'name': 'BillingTiming'
            },
            {
                'name': 'ChargeFunction'
            },
            {
                'name': 'CommitmentType'
            },
            {
                'name': 'ChargeModel'
            },
            {
                'name': 'ChargeModelConfiguration'
            },
            {
                'name': 'CreditOption'
            },
            {
                'name': 'DefaultQuantity'
            },
            {
                'name': 'DeferredRevenueAccount'
            },
            {
                'name': 'DeliverySchedule'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'DiscountLevel'
            },
            {
                'name': 'DrawdownRate'
            },
            {
                'name': 'DrawdownUom'
            },
            {
                'name': 'EndDateCondition'
            },
            {
                'name': 'ExcludeItemBillingFromRevenueAccounting'
            },
            {
                'name': 'ExcludeItemBookingFromRevenueAccounting'
            },
            {
                'name': 'IncludedUnits'
            },
            {
                'name': 'IsAllocationEligible'
            },
            {
                'name': 'IsPrepaid'
            },
            {
                'name': 'IsRollover'
            },
            {
                'name': 'IsStackedDiscount'
            },
            {
                'name': 'IsUnbilled'
            },
            {
                'name': 'LegacyRevenueReporting'
            },
            {
                'name': 'ListPriceBase'
            },
            {
                'name': 'MaxQuantity'
            },
            {
                'name': 'MinQuantity'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'NumberOfPeriod'
            },
            {
                'name': 'OverageCalculationOption'
            },
            {
                'name': 'OverageUnusedUnitsCreditOption'
            },
            {
                'name': 'PrepaidQuantity'
            },
            {
                'name': 'PrepaidUom'
            },
            {
                'name': 'PriceChangeOption'
            },
            {
                'name': 'PriceIncreaseOption'
            },
            {
                'name': 'PriceIncreasePercentage'
            },
            {
                'name': 'ProductCategory'
            },
            {
                'name': 'ProductClass'
            },
            {
                'name': 'ProductFamily'
            },
            {
                'name': 'ProductLine'
            },
            {
                'name': 'RevenueRecognitionTiming'
            },
            {
                'name': 'RevenueAmortizationMethod'
            },
            {
                'name': 'ProductRatePlanChargeNumber'
            },
            {
                'name': 'ProductRatePlanChargeTierData'
            },
            {
                'name': 'ProductRatePlanId'
            },
            {
                'name': 'RatingGroup'
            },
            {
                'name': 'RecognizedRevenueAccount'
            },
            {
                'name': 'RevRecCode'
            },
            {
                'name': 'RevRecTriggerCondition'
            },
            {
                'name': 'RevenueRecognitionRuleName'
            },
            {
                'name': 'RolloverApply'
            },
            {
                'name': 'RolloverPeriods'
            },
            {
                'name': 'SmoothingModel'
            },
            {
                'name': 'SpecificBillingPeriod'
            },
            {
                'name': 'SpecificListPriceBase'
            },
            {
                'name': 'TaxCode'
            },
            {
                'name': 'TaxMode'
            },
            {
                'name': 'Taxable'
            },
            {
                'name': 'TriggerEvent'
            },
            {
                'name': 'UOM'
            },
            {
                'name': 'UpToPeriods'
            },
            {
                'name': 'UpToPeriodsType'
            },
            {
                'name': 'UsageRecordRatingOption'
            },
            {
                'name': 'UseDiscountSpecificAccountingCode'
            },
            {
                'name': 'UseTenantDefaultForPriceChange'
            },
            {
                'name': 'ValidityPeriodType'
            },
            {
                'name': 'WeeklyBillCycleDay'
            },
            {
                'name': 'ApplyToBillingPeriodPartially'
            },
            {
                'name': 'RolloverPeriodLength'
            },
            {
                'name': 'Formula'
            },
            {
                'name': 'Class__NS'
            },
            {
                'name': 'DeferredRevAccount__NS'
            },
            {
                'name': 'Department__NS'
            },
            {
                'name': 'IncludeChildren__NS'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'ItemType__NS'
            },
            {
                'name': 'Location__NS'
            },
            {
                'name': 'RecognizedRevAccount__NS'
            },
            {
                'name': 'RevRecEnd__NS'
            },
            {
                'name': 'RevRecStart__NS'
            },
            {
                'name': 'RevRecTemplateType__NS'
            },
            {
                'name': 'Subsidiary__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/product-rate-plan-charges/{product-rate-plan-charge-key}-GET': {
        'parameters': [
            {
                'name': 'product-rate-plan-charge-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'show-charge-definitions'
            },
        ]
    },
    '/v1/product-rateplan-definitions-POST': {
        'parameters': [
            {
                'name': 'productRatePlanChargeId'
            },
            {
                'name': 'productRatePlanChargeNumber'
            },
            {
                'name': 'productRatePlanId'
            },
            {
                'name': 'productRatePlanNumber'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/product-rateplan-definitions/{product-rateplan-definition-key}-DELETE': {
        'parameters': [
            {
                'name': 'product-rateplan-definition-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/product-rateplan-definitions/{product-rateplan-definition-key}-GET': {
        'parameters': [
            {
                'name': 'product-rateplan-definition-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
        ]
    },
    '/v1/product-rateplan-definitions-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'charge'
            },
            {
                'name': 'rateplan'
            },
        ]
    },
    '/v1/object/product-rate-plan/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/object/product-rate-plan/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/object/product-rate-plan-POST': {
        'parameters': [
            {
                'name': 'ActiveCurrencies'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'EffectiveEndDate'
            },
            {
                'name': 'EffectiveStartDate'
            },
            {
                'name': 'Grade'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'ProductId'
            },
            {
                'name': 'ProductRatePlanNumber'
            },
            {
                'name': 'BillingPeriod__NS'
            },
            {
                'name': 'Class__NS'
            },
            {
                'name': 'Department__NS'
            },
            {
                'name': 'IncludeChildren__NS'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'ItemType__NS'
            },
            {
                'name': 'Location__NS'
            },
            {
                'name': 'MultiCurrencyPrice__NS'
            },
            {
                'name': 'Price__NS'
            },
            {
                'name': 'Subsidiary__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/object/product-rate-plan/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'ActiveCurrencies'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'EffectiveEndDate'
            },
            {
                'name': 'EffectiveStartDate'
            },
            {
                'name': 'Grade'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'ProductId'
            },
            {
                'name': 'ProductRatePlanNumber'
            },
            {
                'name': 'BillingPeriod__NS'
            },
            {
                'name': 'Class__NS'
            },
            {
                'name': 'Department__NS'
            },
            {
                'name': 'IncludeChildren__NS'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'ItemType__NS'
            },
            {
                'name': 'Location__NS'
            },
            {
                'name': 'MultiCurrencyPrice__NS'
            },
            {
                'name': 'Price__NS'
            },
            {
                'name': 'Subsidiary__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/product-rate-plans/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/products/{product-key}/product-rate-plans-GET': {
        'parameters': [
            {
                'name': 'product-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'show-charge-definitions'
            },
        ]
    },
    '/v1/product-rate-plans/external-id/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/object/product/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/object/product/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/object/product-POST': {
        'parameters': [
            {
                'name': 'AllowFeatureChanges'
            },
            {
                'name': 'Category'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'EffectiveEndDate'
            },
            {
                'name': 'EffectiveStartDate'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'ProductNumber'
            },
            {
                'name': 'SKU'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'ItemType__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/object/product/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'AllowFeatureChanges'
            },
            {
                'name': 'Category'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'EffectiveEndDate'
            },
            {
                'name': 'EffectiveStartDate'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'ProductNumber'
            },
            {
                'name': 'SKU'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'ItemType__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/rsa-signatures/decrypt-POST': {
        'parameters': [
            {
                'name': 'method'
            },
            {
                'name': 'publicKey'
            },
            {
                'name': 'signature'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/rsa-signatures-POST': {
        'parameters': [
            {
                'name': 'method'
            },
            {
                'name': 'pageId'
            },
            {
                'name': 'uri'
            },
            {
                'name': 'IBAN'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'authorizationAmount'
            },
            {
                'name': 'bankBranchCode'
            },
            {
                'name': 'bankCheckDigit'
            },
            {
                'name': 'bankCity'
            },
            {
                'name': 'bankPostalCode'
            },
            {
                'name': 'bankStreetName'
            },
            {
                'name': 'bankStreetNumber'
            },
            {
                'name': 'businessIdentificationCode'
            },
            {
                'name': 'cityBlackList'
            },
            {
                'name': 'cityWhiteList'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'deviceSessionId'
            },
            {
                'name': 'gatewayName'
            },
            {
                'name': 'id'
            },
            {
                'name': 'key'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'maxConsecutivePaymentFailures'
            },
            {
                'name': 'param_gwOptions_[*option*]'
            },
            {
                'name': 'param_supportedTypes'
            },
            {
                'name': 'passthrough[1,2,3,4,5]'
            },
            {
                'name': 'paymentGateway'
            },
            {
                'name': 'paymentRetryWindow'
            },
            {
                'name': 'pmId'
            },
            {
                'name': 'signature'
            },
            {
                'name': 'signatureType'
            },
            {
                'name': 'style'
            },
            {
                'name': 'submitEnabled'
            },
            {
                'name': 'tenantId'
            },
            {
                'name': 'token'
            },
            {
                'name': 'useDefaultRetryRule'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/ramps/{rampNumber}-GET': {
        'parameters': [
            {
                'name': 'rampNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/orders/{orderNumber}/ramp-metrics-GET': {
        'parameters': [
            {
                'name': 'orderNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/ramps/{rampNumber}/ramp-metrics-GET': {
        'parameters': [
            {
                'name': 'rampNumber'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/subscriptions/{subscriptionKey}/ramp-metrics-GET': {
        'parameters': [
            {
                'name': 'subscriptionKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/subscriptions/{subscriptionKey}/ramps-GET': {
        'parameters': [
            {
                'name': 'subscriptionKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/rateplans/{ratePlanId}-GET': {
        'parameters': [
            {
                'name': 'ratePlanId'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/refunds/{refundKey}/cancel-PUT': {
        'parameters': [
            {
                'name': 'refundKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/refunds/{refundKey}-GET': {
        'parameters': [
            {
                'name': 'refundKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/refunds/{refundKey}-DELETE': {
        'parameters': [
            {
                'name': 'refundKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/refunds/{refundKey}/parts/{refundpartid}/itemparts/{itempartid}-GET': {
        'parameters': [
            {
                'name': 'itempartid'
            },
            {
                'name': 'refundpartid'
            },
            {
                'name': 'refundKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/refunds/{refundKey}/parts/{refundpartid}/itemparts-GET': {
        'parameters': [
            {
                'name': 'refundpartid'
            },
            {
                'name': 'refundKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/refunds/{refundKey}/parts/{refundpartid}-GET': {
        'parameters': [
            {
                'name': 'refundpartid'
            },
            {
                'name': 'refundKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/refunds/{refundKey}/parts-GET': {
        'parameters': [
            {
                'name': 'refundKey'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/refunds-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'createdById'
            },
            {
                'name': 'createdDate'
            },
            {
                'name': 'methodType'
            },
            {
                'name': 'number'
            },
            {
                'name': 'paymentId'
            },
            {
                'name': 'refundDate'
            },
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'updatedById'
            },
            {
                'name': 'updatedDate'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/v1/refunds/{refundId}-PUT': {
        'parameters': [
            {
                'name': 'refundId'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'financeInformation'
            },
            {
                'name': 'reasonCode'
            },
            {
                'name': 'referenceId'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Origin__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'SynctoNetSuite__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/uno-regenerate/rev-rec-events-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'mode'
            },
            {
                'name': 'forRevenueRecollect'
            },
        ]
    },
    '/v1/uno-regenerate/rev-rec-events/daily-consumption-POST': {
        'parameters': [
            {
                'name': 'originalChargeId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'chargeSegmentNumber'
            },
            {
                'name': 'fundId'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'forRevenueRecollect'
            },
        ]
    },
    '/v1/uno-regenerate/billing-transaction-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'documentId'
            },
            {
                'name': 'number'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'onlyReSend'
            },
            {
                'name': 'reMigrate'
            },
        ]
    },
    '/v1/uno-regenerate/booking-transaction-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'itemNumber'
            },
            {
                'name': 'orderLineItemId'
            },
            {
                'name': 'orderNumber'
            },
            {
                'name': 'subscriptionId'
            },
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'subscriptionVersion'
            },
            {
                'name': 'type'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'onlyReSend'
            },
            {
                'name': 'reMigrate'
            },
        ]
    },
    '/v1/sequence-sets/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/sequence-sets/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'creditMemo'
            },
            {
                'name': 'debitMemo'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'name'
            },
            {
                'name': 'payment'
            },
            {
                'name': 'refund'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/sequence-sets/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/sequence-sets-GET': {
        'parameters': [
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'page'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/v1/sequence-sets-POST': {
        'parameters': [
            {
                'name': 'sequenceSets'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/settings/listing-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/settings/batch-requests-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'requests'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/sign-up-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'accountData'
            },
            {
                'name': 'accountIdentifierField'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'options'
            },
            {
                'name': 'paymentData'
            },
            {
                'name': 'subscriptionData'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/subscriptions/{subscription-key}/cancel-PUT': {
        'parameters': [
            {
                'name': 'cancellationPolicy'
            },
            {
                'name': 'subscription-key'
            },
            {
                'name': 'applicationOrder'
            },
            {
                'name': 'applyCredit'
            },
            {
                'name': 'applyCreditBalance'
            },
            {
                'name': 'bookingDate'
            },
            {
                'name': 'cancellationEffectiveDate'
            },
            {
                'name': 'collect'
            },
            {
                'name': 'contractEffectiveDate'
            },
            {
                'name': 'creditMemoReasonCode'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'invoiceCollect'
            },
            {
                'name': 'invoiceTargetDate'
            },
            {
                'name': 'orderDate'
            },
            {
                'name': 'runBilling'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/subscriptions/{subscription-key}/delete-PUT': {
        'parameters': [
            {
                'name': 'subscription-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/subscriptions/preview-POST': {
        'parameters': [
            {
                'name': 'accountKey'
            },
            {
                'name': 'contractEffectiveDate'
            },
            {
                'name': 'customerAcceptanceDate'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'includeExistingDraftDocItems'
            },
            {
                'name': 'includeExistingDraftInvoiceItems'
            },
            {
                'name': 'initialTerm'
            },
            {
                'name': 'initialTermPeriodType'
            },
            {
                'name': 'invoiceOwnerAccountKey'
            },
            {
                'name': 'invoiceTargetDate'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'previewAccountInfo'
            },
            {
                'name': 'previewType'
            },
            {
                'name': 'serviceActivationDate'
            },
            {
                'name': 'subscribeToRatePlans'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'termStartDate'
            },
            {
                'name': 'termType'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/subscriptions/{subscription-key}/preview-POST': {
        'parameters': [
            {
                'name': 'subscription-key'
            },
            {
                'name': 'previewStartDate'
            },
            {
                'name': 'previewThroughDate'
            },
            {
                'name': 'quantityForUsageCharges'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/subscriptions/{subscription-key}/renew-PUT': {
        'parameters': [
            {
                'name': 'subscription-key'
            },
            {
                'name': 'applicationOrder'
            },
            {
                'name': 'applyCredit'
            },
            {
                'name': 'applyCreditBalance'
            },
            {
                'name': 'collect'
            },
            {
                'name': 'creditMemoReasonCode'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'invoiceCollect'
            },
            {
                'name': 'invoiceTargetDate'
            },
            {
                'name': 'orderDate'
            },
            {
                'name': 'runBilling'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/subscriptions/{subscription-key}/resume-PUT': {
        'parameters': [
            {
                'name': 'resumePolicy'
            },
            {
                'name': 'subscription-key'
            },
            {
                'name': 'applicationOrder'
            },
            {
                'name': 'applyCredit'
            },
            {
                'name': 'applyCreditBalance'
            },
            {
                'name': 'bookingDate'
            },
            {
                'name': 'collect'
            },
            {
                'name': 'contractEffectiveDate'
            },
            {
                'name': 'creditMemoReasonCode'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'extendsTerm'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'invoiceCollect'
            },
            {
                'name': 'invoiceTargetDate'
            },
            {
                'name': 'orderDate'
            },
            {
                'name': 'resumePeriods'
            },
            {
                'name': 'resumePeriodsType'
            },
            {
                'name': 'resumeSpecificDate'
            },
            {
                'name': 'runBilling'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/subscriptions-POST': {
        'parameters': [
            {
                'name': 'accountKey'
            },
            {
                'name': 'applicationOrder'
            },
            {
                'name': 'applyCredit'
            },
            {
                'name': 'applyCreditBalance'
            },
            {
                'name': 'autoRenew'
            },
            {
                'name': 'collect'
            },
            {
                'name': 'contractEffectiveDate'
            },
            {
                'name': 'creditMemoReasonCode'
            },
            {
                'name': 'customerAcceptanceDate'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'externallyManagedBy'
            },
            {
                'name': 'gatewayId'
            },
            {
                'name': 'initialTerm'
            },
            {
                'name': 'initialTermPeriodType'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'invoiceCollect'
            },
            {
                'name': 'invoiceOwnerAccountKey'
            },
            {
                'name': 'invoiceSeparately'
            },
            {
                'name': 'invoiceTargetDate'
            },
            {
                'name': 'lastBookingDate'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'paymentMethodId'
            },
            {
                'name': 'prepayment'
            },
            {
                'name': 'renewalSetting'
            },
            {
                'name': 'renewalTerm'
            },
            {
                'name': 'renewalTermPeriodType'
            },
            {
                'name': 'runBilling'
            },
            {
                'name': 'serviceActivationDate'
            },
            {
                'name': 'subscribeToRatePlans'
            },
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'termStartDate'
            },
            {
                'name': 'termType'
            },
            {
                'name': 'CpqBundleJsonId__QT'
            },
            {
                'name': 'OpportunityCloseDate__QT'
            },
            {
                'name': 'OpportunityName__QT'
            },
            {
                'name': 'QuoteBusinessType__QT'
            },
            {
                'name': 'QuoteNumber__QT'
            },
            {
                'name': 'QuoteType__QT'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Project__NS'
            },
            {
                'name': 'SalesOrder__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/subscriptions/{subscription-key}-PUT': {
        'parameters': [
            {
                'name': 'subscription-key'
            },
            {
                'name': 'add'
            },
            {
                'name': 'applicationOrder'
            },
            {
                'name': 'applyCredit'
            },
            {
                'name': 'applyCreditBalance'
            },
            {
                'name': 'autoRenew'
            },
            {
                'name': 'bookingDate'
            },
            {
                'name': 'change'
            },
            {
                'name': 'collect'
            },
            {
                'name': 'creditMemoReasonCode'
            },
            {
                'name': 'currentTerm'
            },
            {
                'name': 'currentTermPeriodType'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'externallyManagedBy'
            },
            {
                'name': 'includeExistingDraftDocItems'
            },
            {
                'name': 'includeExistingDraftInvoiceItems'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'invoiceCollect'
            },
            {
                'name': 'invoiceSeparately'
            },
            {
                'name': 'invoiceTargetDate'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'preview'
            },
            {
                'name': 'previewType'
            },
            {
                'name': 'remove'
            },
            {
                'name': 'renewalSetting'
            },
            {
                'name': 'renewalTerm'
            },
            {
                'name': 'renewalTermPeriodType'
            },
            {
                'name': 'runBilling'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'termStartDate'
            },
            {
                'name': 'termType'
            },
            {
                'name': 'update'
            },
            {
                'name': 'CpqBundleJsonId__QT'
            },
            {
                'name': 'OpportunityCloseDate__QT'
            },
            {
                'name': 'OpportunityName__QT'
            },
            {
                'name': 'QuoteBusinessType__QT'
            },
            {
                'name': 'QuoteNumber__QT'
            },
            {
                'name': 'QuoteType__QT'
            },
            {
                'name': 'IntegrationId__NS'
            },
            {
                'name': 'IntegrationStatus__NS'
            },
            {
                'name': 'Project__NS'
            },
            {
                'name': 'SalesOrder__NS'
            },
            {
                'name': 'SyncDate__NS'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/subscriptions/accounts/{account-key}-GET': {
        'parameters': [
            {
                'name': 'account-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'charge-detail'
            },
            {
                'name': 'exclude-rate-plans-with-no-charges'
            },
        ]
    },
    '/v1/subscriptions/{subscription-key}-GET': {
        'parameters': [
            {
                'name': 'subscription-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'charge-detail'
            },
            {
                'name': 'exclude-rate-plans-with-no-charges'
            },
        ]
    },
    '/v1/subscriptions/{subscription-key}/versions/{version}-GET': {
        'parameters': [
            {
                'name': 'subscription-key'
            },
            {
                'name': 'version'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'charge-detail'
            },
            {
                'name': 'exclude-rate-plans-with-no-charges'
            },
            {
                'name': 'getDetailedMetrics'
            },
            {
                'name': 'asOfDay'
            },
        ]
    },
    '/v1/subscriptions/{subscription-key}/suspend-PUT': {
        'parameters': [
            {
                'name': 'suspendPolicy'
            },
            {
                'name': 'subscription-key'
            },
            {
                'name': 'applicationOrder'
            },
            {
                'name': 'applyCredit'
            },
            {
                'name': 'applyCreditBalance'
            },
            {
                'name': 'bookingDate'
            },
            {
                'name': 'collect'
            },
            {
                'name': 'contractEffectiveDate'
            },
            {
                'name': 'creditMemoReasonCode'
            },
            {
                'name': 'documentDate'
            },
            {
                'name': 'extendsTerm'
            },
            {
                'name': 'invoice'
            },
            {
                'name': 'invoiceCollect'
            },
            {
                'name': 'invoiceTargetDate'
            },
            {
                'name': 'orderDate'
            },
            {
                'name': 'resume'
            },
            {
                'name': 'resumePeriods'
            },
            {
                'name': 'resumePeriodsType'
            },
            {
                'name': 'resumePolicy'
            },
            {
                'name': 'resumeSpecificDate'
            },
            {
                'name': 'runBilling'
            },
            {
                'name': 'suspendPeriods'
            },
            {
                'name': 'suspendPeriodsType'
            },
            {
                'name': 'suspendSpecificDate'
            },
            {
                'name': 'targetDate'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'zuora-version'
            },
        ]
    },
    '/v1/subscriptions/{subscriptionNumber}/versions/{version}/customFields-PUT': {
        'parameters': [
            {
                'name': 'subscriptionNumber'
            },
            {
                'name': 'version'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'ratePlans'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/journal-entries/journal-runs/{jr-number}-GET': {
        'parameters': [
            {
                'name': 'jr-number'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/journal-entries/{je-number}/basic-information-PUT': {
        'parameters': [
            {
                'name': 'je-number'
            },
            {
                'name': 'journalEntryItems'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'transferredToAccounting'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/journal-entries-POST': {
        'parameters': [
            {
                'name': 'accountingPeriodName'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'journalEntryDate'
            },
            {
                'name': 'journalEntryItems'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'organizationLabel'
            },
            {
                'name': 'segments'
            },
            {
                'name': 'transferredToAccounting'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/journal-entries/{je-number}-GET': {
        'parameters': [
            {
                'name': 'je-number'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/journal-entries/{je-number}-DELETE': {
        'parameters': [
            {
                'name': 'je-number'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/journal-entries/{je-number}/cancel-PUT': {
        'parameters': [
            {
                'name': 'je-number'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/object/taxation-item-POST': {
        'parameters': [
            {
                'name': 'AccountingCode'
            },
            {
                'name': 'ExemptAmount'
            },
            {
                'name': 'InvoiceItemId'
            },
            {
                'name': 'Jurisdiction'
            },
            {
                'name': 'LocationCode'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'TaxAmount'
            },
            {
                'name': 'TaxCode'
            },
            {
                'name': 'TaxCodeDescription'
            },
            {
                'name': 'TaxDate'
            },
            {
                'name': 'TaxRate'
            },
            {
                'name': 'TaxRateDescription'
            },
            {
                'name': 'TaxRateType'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/taxationitems/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/taxationitems/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'exemptAmount'
            },
            {
                'name': 'financeInformation'
            },
            {
                'name': 'jurisdiction'
            },
            {
                'name': 'locationCode'
            },
            {
                'name': 'name'
            },
            {
                'name': 'taxAmount'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'taxCodeDescription'
            },
            {
                'name': 'taxDate'
            },
            {
                'name': 'taxRate'
            },
            {
                'name': 'taxRateDescription'
            },
            {
                'name': 'taxRateType'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/taxationitems/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/object/usage/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/object/usage/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v1/invoices/invoice-item/{invoice-item-id}/usage-rate-detail-GET': {
        'parameters': [
            {
                'name': 'invoice-item-id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/object/usage-POST': {
        'parameters': [
            {
                'name': 'AccountId'
            },
            {
                'name': 'AccountNumber'
            },
            {
                'name': 'ChargeId'
            },
            {
                'name': 'ChargeNumber'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'EndDateTime'
            },
            {
                'name': 'Quantity'
            },
            {
                'name': 'StartDateTime'
            },
            {
                'name': 'SubscriptionId'
            },
            {
                'name': 'SubscriptionNumber'
            },
            {
                'name': 'UOM'
            },
            {
                'name': 'UniqueKey'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'X-Zuora-WSDL-Version'
            },
        ]
    },
    '/v1/object/usage/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'EndDateTime'
            },
            {
                'name': 'Quantity'
            },
            {
                'name': 'RbeStatus'
            },
            {
                'name': 'StartDateTime'
            },
            {
                'name': 'UOM'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'rejectUnknownFields'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/usage-POST': {
        'parameters': [
            {
                'name': 'file'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/v1/usage/accounts/{account-key}-GET': {
        'parameters': [
            {
                'name': 'account-key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/workflows/workflow_runs/{workflow_run_id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'workflow_run_id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/{workflow_id}/run-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'workflow_id'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'paymentId'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/workflow_runs/{workflow_run_id}/stop-PUT': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'workflow_run_id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/{workflow_id}-PATCH': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'workflow_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active_workflow_version_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
        ]
    },
    '/workflows/{workflow_id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'workflow_id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/{workflow_id}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'workflow_id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/{workflow_id}/export-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'workflow_id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/workflows/import-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'linkages'
            },
            {
                'name': 'tasks'
            },
            {
                'name': 'workflow'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'workflow_definition_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'activate'
            },
        ]
    },
    '/versions/{version_id}-DELETE': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'version_id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/{workflow_id}/versions-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'workflow_id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/{workflow_id}/versions/import-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'workflow_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'linkages'
            },
            {
                'name': 'tasks'
            },
            {
                'name': 'workflow'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'activate'
            },
        ]
    },
    '/workflows-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'callout_trigger'
            },
            {
                'name': 'interval'
            },
            {
                'name': 'name'
            },
            {
                'name': 'ondemand_trigger'
            },
            {
                'name': 'scheduled_trigger'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_length'
            },
        ]
    },
    '/workflows/tasks/{task_id}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/tasks/{task_id}/rerun-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/tasks-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'instance'
            },
            {
                'name': 'action_type'
            },
            {
                'name': 'object'
            },
            {
                'name': 'object_id'
            },
            {
                'name': 'call_type'
            },
            {
                'name': 'workflow_id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_length'
            },
        ]
    },
    '/workflows/tasks/batch_update-PUT': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'data'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/workflows/metrics.json-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'metrics'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
    '/v1/revpro-accounting-codes-PUT': {
        'parameters': [
            {
                'name': 'adjustmentLiabilityAccount'
            },
            {
                'name': 'adjustmentRevenueAccount'
            },
            {
                'name': 'contractAssetAccount'
            },
            {
                'name': 'contractLiabilityAccount'
            },
            {
                'name': 'productRatePlanChargeId'
            },
            {
                'name': 'recognizedRevenueAccount'
            },
            {
                'name': 'unbilledReceivablesAccount'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'Accept-Encoding'
            },
            {
                'name': 'Content-Encoding'
            },
            {
                'name': 'Zuora-Entity-Ids'
            },
            {
                'name': 'Zuora-Org-Ids'
            },
            {
                'name': 'Zuora-Track-Id'
            },
        ]
    },
};
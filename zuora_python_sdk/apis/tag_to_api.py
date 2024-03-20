import typing_extensions

from zuora_python_sdk.apis.tags import TagValues
from zuora_python_sdk.apis.tags.credit_memos_api import CreditMemosApi
from zuora_python_sdk.apis.tags.debit_memos_api import DebitMemosApi
from zuora_python_sdk.apis.tags.invoices_api import InvoicesApi
from zuora_python_sdk.apis.tags.orders_api import OrdersApi
from zuora_python_sdk.apis.tags.notifications_api import NotificationsApi
from zuora_python_sdk.apis.tags.workflows_api import WorkflowsApi
from zuora_python_sdk.apis.tags.e_invoicing_api import EInvoicingApi
from zuora_python_sdk.apis.tags.payment_methods_api import PaymentMethodsApi
from zuora_python_sdk.apis.tags.payments_api import PaymentsApi
from zuora_python_sdk.apis.tags.payment_schedules_api import PaymentSchedulesApi
from zuora_python_sdk.apis.tags.subscriptions_api import SubscriptionsApi
from zuora_python_sdk.apis.tags.accounting_periods_api import AccountingPeriodsApi
from zuora_python_sdk.apis.tags.data_backfill_api import DataBackfillApi
from zuora_python_sdk.apis.tags.refunds_api import RefundsApi
from zuora_python_sdk.apis.tags.configuration_templates_api import ConfigurationTemplatesApi
from zuora_python_sdk.apis.tags.fulfillments_api import FulfillmentsApi
from zuora_python_sdk.apis.tags.accounting_codes_api import AccountingCodesApi
from zuora_python_sdk.apis.tags.accounts_api import AccountsApi
from zuora_python_sdk.apis.tags.custom_object_records_api import CustomObjectRecordsApi
from zuora_python_sdk.apis.tags.invoice_schedules_api import InvoiceSchedulesApi
from zuora_python_sdk.apis.tags.payment_runs_api import PaymentRunsApi
from zuora_python_sdk.apis.tags.product_charge_definitions_api import ProductChargeDefinitionsApi
from zuora_python_sdk.apis.tags.product_rate_plans_api import ProductRatePlansApi
from zuora_python_sdk.apis.tags.usage_api import UsageApi
from zuora_python_sdk.apis.tags.bill_run_api import BillRunApi
from zuora_python_sdk.apis.tags.metadata_api import MetadataApi
from zuora_python_sdk.apis.tags.custom_object_jobs_api import CustomObjectJobsApi
from zuora_python_sdk.apis.tags.summary_journal_entries_api import SummaryJournalEntriesApi
from zuora_python_sdk.apis.tags.actions_api import ActionsApi
from zuora_python_sdk.apis.tags.delivery_adjustments_api import DeliveryAdjustmentsApi
from zuora_python_sdk.apis.tags.attachments_api import AttachmentsApi
from zuora_python_sdk.apis.tags.catalog_groups_api import CatalogGroupsApi
from zuora_python_sdk.apis.tags.contacts_api import ContactsApi
from zuora_python_sdk.apis.tags.custom_event_triggers_api import CustomEventTriggersApi
from zuora_python_sdk.apis.tags.custom_object_definitions_api import CustomObjectDefinitionsApi
from zuora_python_sdk.apis.tags.custom_payment_method_types_api import CustomPaymentMethodTypesApi
from zuora_python_sdk.apis.tags.custom_scheduled_events_api import CustomScheduledEventsApi
from zuora_python_sdk.apis.tags.operations_api import OperationsApi
from zuora_python_sdk.apis.tags.product_rate_plan_charges_api import ProductRatePlanChargesApi
from zuora_python_sdk.apis.tags.ramps_api import RampsApi
from zuora_python_sdk.apis.tags.sequence_sets_api import SequenceSetsApi
from zuora_python_sdk.apis.tags.aggregate_queries_api import AggregateQueriesApi
from zuora_python_sdk.apis.tags.billing_documents_api import BillingDocumentsApi
from zuora_python_sdk.apis.tags.data_queries_api import DataQueriesApi
from zuora_python_sdk.apis.tags.journal_runs_api import JournalRunsApi
from zuora_python_sdk.apis.tags.payment_gateway_reconciliation_api import PaymentGatewayReconciliationApi
from zuora_python_sdk.apis.tags.product_rate_plan_definitions_api import ProductRatePlanDefinitionsApi
from zuora_python_sdk.apis.tags.products_api import ProductsApi
from zuora_python_sdk.apis.tags.regenerate_api import RegenerateApi
from zuora_python_sdk.apis.tags.taxation_items_api import TaxationItemsApi
from zuora_python_sdk.apis.tags.mass_updater_api import MassUpdaterApi
from zuora_python_sdk.apis.tags.order_line_items_api import OrderLineItemsApi
from zuora_python_sdk.apis.tags.prepaid_with_drawdown_api import PrepaidWithDrawdownApi
from zuora_python_sdk.apis.tags.billing_preview_run_api import BillingPreviewRunApi
from zuora_python_sdk.apis.tags.catalog_api import CatalogApi
from zuora_python_sdk.apis.tags.data_labeling_api import DataLabelingApi
from zuora_python_sdk.apis.tags.imports_api import ImportsApi
from zuora_python_sdk.apis.tags.payment_method_updater_api import PaymentMethodUpdaterApi
from zuora_python_sdk.apis.tags.payment_authorization_api import PaymentAuthorizationApi
from zuora_python_sdk.apis.tags.product_rate_plan_charge_tiers_api import ProductRatePlanChargeTiersApi
from zuora_python_sdk.apis.tags.rsa_signatures_api import RSASignaturesApi
from zuora_python_sdk.apis.tags.settings_api import SettingsApi
from zuora_python_sdk.apis.tags.api_health_api import APIHealthApi
from zuora_python_sdk.apis.tags.bill_run_health_api import BillRunHealthApi
from zuora_python_sdk.apis.tags.contact_snapshots_api import ContactSnapshotsApi
from zuora_python_sdk.apis.tags.custom_exchange_rates_api import CustomExchangeRatesApi
from zuora_python_sdk.apis.tags.describe_api import DescribeApi
from zuora_python_sdk.apis.tags.electronic_payments_health_api import ElectronicPaymentsHealthApi
from zuora_python_sdk.apis.tags.files_api import FilesApi
from zuora_python_sdk.apis.tags.hosted_pages_api import HostedPagesApi
from zuora_python_sdk.apis.tags.o_auth_api import OAuthApi
from zuora_python_sdk.apis.tags.order_actions_api import OrderActionsApi
from zuora_python_sdk.apis.tags.payment_gateways_api import PaymentGatewaysApi
from zuora_python_sdk.apis.tags.payment_method_snapshots_api import PaymentMethodSnapshotsApi
from zuora_python_sdk.apis.tags.payment_method_transaction_logs_api import PaymentMethodTransactionLogsApi
from zuora_python_sdk.apis.tags.payment_transaction_logs_api import PaymentTransactionLogsApi
from zuora_python_sdk.apis.tags.rate_plans_api import RatePlansApi
from zuora_python_sdk.apis.tags.sign_up_api import SignUpApi
from zuora_python_sdk.apis.tags.zuora_revenue_integration_api import ZuoraRevenueIntegrationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CREDIT_MEMOS: CreditMemosApi,
        TagValues.DEBIT_MEMOS: DebitMemosApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.EINVOICING: EInvoicingApi,
        TagValues.PAYMENT_METHODS: PaymentMethodsApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.PAYMENT_SCHEDULES: PaymentSchedulesApi,
        TagValues.SUBSCRIPTIONS: SubscriptionsApi,
        TagValues.ACCOUNTING_PERIODS: AccountingPeriodsApi,
        TagValues.DATA_BACKFILL: DataBackfillApi,
        TagValues.REFUNDS: RefundsApi,
        TagValues.CONFIGURATION_TEMPLATES: ConfigurationTemplatesApi,
        TagValues.FULFILLMENTS: FulfillmentsApi,
        TagValues.ACCOUNTING_CODES: AccountingCodesApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CUSTOM_OBJECT_RECORDS: CustomObjectRecordsApi,
        TagValues.INVOICE_SCHEDULES: InvoiceSchedulesApi,
        TagValues.PAYMENT_RUNS: PaymentRunsApi,
        TagValues.PRODUCT_CHARGE_DEFINITIONS: ProductChargeDefinitionsApi,
        TagValues.PRODUCT_RATE_PLANS: ProductRatePlansApi,
        TagValues.USAGE: UsageApi,
        TagValues.BILL_RUN: BillRunApi,
        TagValues.METADATA: MetadataApi,
        TagValues.CUSTOM_OBJECT_JOBS: CustomObjectJobsApi,
        TagValues.SUMMARY_JOURNAL_ENTRIES: SummaryJournalEntriesApi,
        TagValues.ACTIONS: ActionsApi,
        TagValues.DELIVERY_ADJUSTMENTS: DeliveryAdjustmentsApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.CATALOG_GROUPS: CatalogGroupsApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.CUSTOM_EVENT_TRIGGERS: CustomEventTriggersApi,
        TagValues.CUSTOM_OBJECT_DEFINITIONS: CustomObjectDefinitionsApi,
        TagValues.CUSTOM_PAYMENT_METHOD_TYPES: CustomPaymentMethodTypesApi,
        TagValues.CUSTOM_SCHEDULED_EVENTS: CustomScheduledEventsApi,
        TagValues.OPERATIONS: OperationsApi,
        TagValues.PRODUCT_RATE_PLAN_CHARGES: ProductRatePlanChargesApi,
        TagValues.RAMPS: RampsApi,
        TagValues.SEQUENCE_SETS: SequenceSetsApi,
        TagValues.AGGREGATE_QUERIES: AggregateQueriesApi,
        TagValues.BILLING_DOCUMENTS: BillingDocumentsApi,
        TagValues.DATA_QUERIES: DataQueriesApi,
        TagValues.JOURNAL_RUNS: JournalRunsApi,
        TagValues.PAYMENT_GATEWAY_RECONCILIATION: PaymentGatewayReconciliationApi,
        TagValues.PRODUCT_RATE_PLAN_DEFINITIONS: ProductRatePlanDefinitionsApi,
        TagValues.PRODUCTS: ProductsApi,
        TagValues.REGENERATE: RegenerateApi,
        TagValues.TAXATION_ITEMS: TaxationItemsApi,
        TagValues.MASS_UPDATER: MassUpdaterApi,
        TagValues.ORDER_LINE_ITEMS: OrderLineItemsApi,
        TagValues.PREPAID_WITH_DRAWDOWN: PrepaidWithDrawdownApi,
        TagValues.BILLING_PREVIEW_RUN: BillingPreviewRunApi,
        TagValues.CATALOG: CatalogApi,
        TagValues.DATA_LABELING: DataLabelingApi,
        TagValues.IMPORTS: ImportsApi,
        TagValues.PAYMENT_METHOD_UPDATER: PaymentMethodUpdaterApi,
        TagValues.PAYMENT_AUTHORIZATION: PaymentAuthorizationApi,
        TagValues.PRODUCT_RATE_PLAN_CHARGE_TIERS: ProductRatePlanChargeTiersApi,
        TagValues.RSA_SIGNATURES: RSASignaturesApi,
        TagValues.SETTINGS: SettingsApi,
        TagValues.API_HEALTH: APIHealthApi,
        TagValues.BILL_RUN_HEALTH: BillRunHealthApi,
        TagValues.CONTACT_SNAPSHOTS: ContactSnapshotsApi,
        TagValues.CUSTOM_EXCHANGE_RATES: CustomExchangeRatesApi,
        TagValues.DESCRIBE: DescribeApi,
        TagValues.ELECTRONIC_PAYMENTS_HEALTH: ElectronicPaymentsHealthApi,
        TagValues.FILES: FilesApi,
        TagValues.HOSTED_PAGES: HostedPagesApi,
        TagValues.OAUTH: OAuthApi,
        TagValues.ORDER_ACTIONS: OrderActionsApi,
        TagValues.PAYMENT_GATEWAYS: PaymentGatewaysApi,
        TagValues.PAYMENT_METHOD_SNAPSHOTS: PaymentMethodSnapshotsApi,
        TagValues.PAYMENT_METHOD_TRANSACTION_LOGS: PaymentMethodTransactionLogsApi,
        TagValues.PAYMENT_TRANSACTION_LOGS: PaymentTransactionLogsApi,
        TagValues.RATE_PLANS: RatePlansApi,
        TagValues.SIGN_UP: SignUpApi,
        TagValues.ZUORA_REVENUE_INTEGRATION: ZuoraRevenueIntegrationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CREDIT_MEMOS: CreditMemosApi,
        TagValues.DEBIT_MEMOS: DebitMemosApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.EINVOICING: EInvoicingApi,
        TagValues.PAYMENT_METHODS: PaymentMethodsApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.PAYMENT_SCHEDULES: PaymentSchedulesApi,
        TagValues.SUBSCRIPTIONS: SubscriptionsApi,
        TagValues.ACCOUNTING_PERIODS: AccountingPeriodsApi,
        TagValues.DATA_BACKFILL: DataBackfillApi,
        TagValues.REFUNDS: RefundsApi,
        TagValues.CONFIGURATION_TEMPLATES: ConfigurationTemplatesApi,
        TagValues.FULFILLMENTS: FulfillmentsApi,
        TagValues.ACCOUNTING_CODES: AccountingCodesApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CUSTOM_OBJECT_RECORDS: CustomObjectRecordsApi,
        TagValues.INVOICE_SCHEDULES: InvoiceSchedulesApi,
        TagValues.PAYMENT_RUNS: PaymentRunsApi,
        TagValues.PRODUCT_CHARGE_DEFINITIONS: ProductChargeDefinitionsApi,
        TagValues.PRODUCT_RATE_PLANS: ProductRatePlansApi,
        TagValues.USAGE: UsageApi,
        TagValues.BILL_RUN: BillRunApi,
        TagValues.METADATA: MetadataApi,
        TagValues.CUSTOM_OBJECT_JOBS: CustomObjectJobsApi,
        TagValues.SUMMARY_JOURNAL_ENTRIES: SummaryJournalEntriesApi,
        TagValues.ACTIONS: ActionsApi,
        TagValues.DELIVERY_ADJUSTMENTS: DeliveryAdjustmentsApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.CATALOG_GROUPS: CatalogGroupsApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.CUSTOM_EVENT_TRIGGERS: CustomEventTriggersApi,
        TagValues.CUSTOM_OBJECT_DEFINITIONS: CustomObjectDefinitionsApi,
        TagValues.CUSTOM_PAYMENT_METHOD_TYPES: CustomPaymentMethodTypesApi,
        TagValues.CUSTOM_SCHEDULED_EVENTS: CustomScheduledEventsApi,
        TagValues.OPERATIONS: OperationsApi,
        TagValues.PRODUCT_RATE_PLAN_CHARGES: ProductRatePlanChargesApi,
        TagValues.RAMPS: RampsApi,
        TagValues.SEQUENCE_SETS: SequenceSetsApi,
        TagValues.AGGREGATE_QUERIES: AggregateQueriesApi,
        TagValues.BILLING_DOCUMENTS: BillingDocumentsApi,
        TagValues.DATA_QUERIES: DataQueriesApi,
        TagValues.JOURNAL_RUNS: JournalRunsApi,
        TagValues.PAYMENT_GATEWAY_RECONCILIATION: PaymentGatewayReconciliationApi,
        TagValues.PRODUCT_RATE_PLAN_DEFINITIONS: ProductRatePlanDefinitionsApi,
        TagValues.PRODUCTS: ProductsApi,
        TagValues.REGENERATE: RegenerateApi,
        TagValues.TAXATION_ITEMS: TaxationItemsApi,
        TagValues.MASS_UPDATER: MassUpdaterApi,
        TagValues.ORDER_LINE_ITEMS: OrderLineItemsApi,
        TagValues.PREPAID_WITH_DRAWDOWN: PrepaidWithDrawdownApi,
        TagValues.BILLING_PREVIEW_RUN: BillingPreviewRunApi,
        TagValues.CATALOG: CatalogApi,
        TagValues.DATA_LABELING: DataLabelingApi,
        TagValues.IMPORTS: ImportsApi,
        TagValues.PAYMENT_METHOD_UPDATER: PaymentMethodUpdaterApi,
        TagValues.PAYMENT_AUTHORIZATION: PaymentAuthorizationApi,
        TagValues.PRODUCT_RATE_PLAN_CHARGE_TIERS: ProductRatePlanChargeTiersApi,
        TagValues.RSA_SIGNATURES: RSASignaturesApi,
        TagValues.SETTINGS: SettingsApi,
        TagValues.API_HEALTH: APIHealthApi,
        TagValues.BILL_RUN_HEALTH: BillRunHealthApi,
        TagValues.CONTACT_SNAPSHOTS: ContactSnapshotsApi,
        TagValues.CUSTOM_EXCHANGE_RATES: CustomExchangeRatesApi,
        TagValues.DESCRIBE: DescribeApi,
        TagValues.ELECTRONIC_PAYMENTS_HEALTH: ElectronicPaymentsHealthApi,
        TagValues.FILES: FilesApi,
        TagValues.HOSTED_PAGES: HostedPagesApi,
        TagValues.OAUTH: OAuthApi,
        TagValues.ORDER_ACTIONS: OrderActionsApi,
        TagValues.PAYMENT_GATEWAYS: PaymentGatewaysApi,
        TagValues.PAYMENT_METHOD_SNAPSHOTS: PaymentMethodSnapshotsApi,
        TagValues.PAYMENT_METHOD_TRANSACTION_LOGS: PaymentMethodTransactionLogsApi,
        TagValues.PAYMENT_TRANSACTION_LOGS: PaymentTransactionLogsApi,
        TagValues.RATE_PLANS: RatePlansApi,
        TagValues.SIGN_UP: SignUpApi,
        TagValues.ZUORA_REVENUE_INTEGRATION: ZuoraRevenueIntegrationApi,
    }
)

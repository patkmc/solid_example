from abc import ABC, abstractmethod


# with applying open–closed principle:


class BaseDocumentService(ABC):
    @abstractmethod
    def determine_document_type(self, document: str) -> str:
        pass

    @abstractmethod
    def auth_with_api_key(self) -> bool:
        pass


class InternalDocumentService(BaseDocumentService):
    def determine_document_type(self, document: str) -> str:
        pass

    def auth_with_api_key(self) -> bool:
        raise Exception("Authentication not needed")


class ExternalDocumentService(BaseDocumentService):
    def determine_document_type(self, document: str) -> str:
        pass

    def auth_with_api_key(self) -> bool:
        pass


class BaseDocumentDataFetcher(ABC):
    @abstractmethod
    def fetch_data(self, document: str, field_to_fetch: str) -> str:
        pass


class PaymentOrderDataFetcher(BaseDocumentDataFetcher):
    def fetch_data(self, document: str, field_to_fetch: str) -> str:
        if field_to_fetch == "sygnatura_akt":
            return self._fetch_payment_order_signature(document)
        elif field_to_fetch == "data_pisma":
            return self._fetch_payment_order_document_data(document)

    def _fetch_payment_order_signature(self, document: str) -> str:
        pass

    def _fetch_payment_order_document_data(self, document: str) -> str:
        pass


class BailiffDecisionDataFetcher(BaseDocumentDataFetcher):
    def fetch_data(self, document: str, field_to_fetch: str) -> str:
        pass


data_fetchers = {
    "nakaz_zaplaty": PaymentOrderDataFetcher(),
    "postanowienie_komornicze": BailiffDecisionDataFetcher()
}


def fetch_field(document: str, field_to_fetch: str, doc_service: InternalDocumentService) -> str:
    document_type = doc_service.determine_document_type(document)
    data_fetcher = data_fetchers[document_type]
    return data_fetcher.fetch_data(document, field_to_fetch)


_document = "some very important text"
_field_to_fetch = "sygnatura_akt"
fetch_field(_document, _field_to_fetch, InternalDocumentService())

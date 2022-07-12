# with applying Single responsibility principle
class DocumentService:
    def determine_document_type(self, document: str) -> str:
        pass


class DocumentDataFetcher:
    def fetch_data(self, document_type: str, document: str, field_to_fetch: str) -> str:
        if document_type == "nakaz_zaplaty":
            if field_to_fetch == "sygnatura_akt":
                return self._fetch_payment_order_signature(document)
            elif field_to_fetch == "data_pisma":
                return self._fetch_payment_order_document_data(document)
        elif document_type == "postanowienie_komornicze":
            pass

    def _fetch_payment_order_signature(self, document: str) -> str:
        pass

    def _fetch_payment_order_document_data(self, document: str) -> str:
        pass


def fetch_field(document: str, field_to_fetch: str) -> str:
    document_type = DocumentService().determine_document_type(document)
    return DocumentDataFetcher().fetch_data(document_type, document, field_to_fetch)


_document = "some very important text"
_field_to_fetch = "sygnatura_akt"
_result = fetch_field(_document, _field_to_fetch)

class DocumentDataFetcher:
    def fetch_data(self, document: str, field_to_fetch: str) -> str:
        document_type = self._determine_document_type(document)
        if document_type == "nakaz_zaplaty":
            if field_to_fetch == "sygnatura_akt":
                return self._fetch_payment_order_signature(document)
            elif field_to_fetch == "data_pisma":
                return self._fetch_payment_order_document_data(document)
        elif document_type == "postanowienie_komornicze":
            pass

    def _determine_document_type(self, document: str) -> str:
        pass

    def _fetch_payment_order_signature(self, document: str) -> str:
        pass

    def _fetch_payment_order_document_data(self, document: str) -> str:
        pass


def fetch_field(document: str, field_to_fetch: str) -> str:
    return DocumentDataFetcher().fetch_data(document, field_to_fetch)


_document = "some very important text"
_field_to_fetch = "sygnatura_akt"
_result = fetch_field(_document, _field_to_fetch)
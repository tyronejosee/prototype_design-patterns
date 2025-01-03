from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Document(ABC):
    """Interface for documents."""

    @abstractmethod
    def accept(self, visitor: DocumentVisitor) -> None:
        pass


class Invoice(Document):
    """Class representing an invoice."""

    def accept(self, visitor: DocumentVisitor) -> None:
        visitor.visit_invoice(self)

    def get_invoice_data(self) -> dict:
        return {"id": 1, "customer": "John Doe", "total": 150.50}


class Receipt(Document):
    """Class representing a receipt."""

    def accept(self, visitor: DocumentVisitor) -> None:
        visitor.visit_receipt(self)

    def get_receipt_data(self) -> dict:
        return {"id": 101, "store": "Tech Store", "amount_paid": 75.25}


class PurchaseOrder(Document):
    """Class representing a purchase order."""

    def accept(self, visitor: DocumentVisitor) -> None:
        visitor.visit_purchase_order(self)

    def get_purchase_order_data(self) -> dict:
        return {
            "id": 202,
            "supplier": "Office Supplies Co.",
            "items": 5,
            "total": 300.00,
        }


class DocumentVisitor(ABC):
    """Visitor interface for exporting documents."""

    @abstractmethod
    def visit_invoice(self, invoice: Invoice) -> None:
        pass

    @abstractmethod
    def visit_receipt(self, receipt: Receipt) -> None:
        pass

    @abstractmethod
    def visit_purchase_order(self, purchase_order: PurchaseOrder) -> None:
        pass


class JSONExportVisitor(DocumentVisitor):
    """Export documents in JSON format."""

    def visit_invoice(self, invoice: Invoice) -> None:
        print("Exporting Invoice in JSON:")
        print(invoice.get_invoice_data())

    def visit_receipt(self, receipt: Receipt) -> None:
        print("Exporting Receipt in JSON:")
        print(receipt.get_receipt_data())

    def visit_purchase_order(self, purchase_order: PurchaseOrder) -> None:
        print("Exporting Purchase Order in JSON:")
        print(purchase_order.get_purchase_order_data())


class XMLExportVisitor(DocumentVisitor):
    """Export documents in XML format."""

    def visit_invoice(self, invoice: Invoice) -> None:
        print("Exporting Invoice in XML:")
        data = invoice.get_invoice_data()
        print(
            f"<invoice><id>{data['id']}</id><customer>{data['customer']}</customer><total>{data['total']}</total></invoice>"
        )

    def visit_receipt(self, receipt: Receipt) -> None:
        print("Exporting Receipt in XML:")
        data = receipt.get_receipt_data()
        print(
            f"<receipt><id>{data['id']}</id><store>{data['store']}</store><amount_paid>{data['amount_paid']}</amount_paid></receipt>"
        )

    def visit_purchase_order(self, purchase_order: PurchaseOrder) -> None:
        print("Exporting Purchase Order in XML:")
        data = purchase_order.get_purchase_order_data()
        print(
            f"<purchase_order><id>{data['id']}</id><supplier>{data['supplier']}</supplier><items>{data['items']}</items><total>{data['total']}</total></purchase_order>"
        )


def client_code(documents: List[Document], visitor: DocumentVisitor) -> None:
    """Applies a visitor to a list of documents."""
    for document in documents:
        document.accept(visitor)


if __name__ == "__main__":
    documents: List[Document] = [Invoice(), Receipt(), PurchaseOrder()]

    print("Exporting documents in JSON format:")
    json_visitor = JSONExportVisitor()
    client_code(documents, json_visitor)

    print("\nExporting documents in XML format:")
    xml_visitor = XMLExportVisitor()
    client_code(documents, xml_visitor)

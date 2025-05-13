import requests
import json
from typing import List, Dict, Tuple


class ProductDataValidator:
    """API Testing class for validating product data from fakestoreapi"""

    def __init__(self, api_url: str = "https://fakestoreapi.com/products"):
        self.api_url = api_url
        self.products = []
        self.defects = []

    def fetch_products(self) -> Tuple[int, List[Dict]]:
        """Fetch products from the API and return status code and data"""
        try:
            response = requests.get(self.api_url)
            self.products = response.json() if response.status_code == 200 else []
            return response.status_code, self.products
        except Exception as e:
            print(f"Error fetching data: {e}")
            return 0, []

    def validate_response_code(self, status_code: int) -> bool:
        """Verify server response code is 200"""
        is_valid = status_code == 200
        if not is_valid:
            self.defects.append({
                "type": "API Response Error",
                "product_id": None,
                "error": f"Expected status code 200, got {status_code}"
            })
        return is_valid

    def validate_product(self, product: Dict, index: int) -> List[str]:
        """Validate a single product and return list of defects"""
        defects = []
        product_id = product.get('id', f'Unknown (index {index})')

        # Check if title exists and is not empty
        if 'title' not in product:
            defects.append(f"Missing 'title' attribute")
        elif not product['title'] or product['title'].strip() == '':
            defects.append(f"Empty 'title' attribute")

        # Check if price exists and is not negative
        if 'price' not in product:
            defects.append(f"Missing 'price' attribute")
        else:
            try:
                price = float(product['price'])
                if price < 0:
                    defects.append(f"Negative price: {price}")
            except (ValueError, TypeError):
                defects.append(f"Invalid price format: {product['price']}")

        # Check if rating.rate exists and doesn't exceed 5
        if 'rating' not in product:
            defects.append(f"Missing 'rating' attribute")
        elif isinstance(product['rating'], dict):
            if 'rate' not in product['rating']:
                defects.append(f"Missing 'rating.rate' attribute")
            else:
                try:
                    rate = float(product['rating']['rate'])
                    if rate > 5:
                        defects.append(f"Rating exceeds 5: {rate}")
                    elif rate < 0:
                        defects.append(f"Negative rating: {rate}")
                except (ValueError, TypeError):
                    defects.append(f"Invalid rating format: {product['rating']['rate']}")
        else:
            defects.append(f"Invalid 'rating' structure")

        # Log defects for this product
        for defect in defects:
            self.defects.append({
                "type": "Product Validation Error",
                "product_id": product_id,
                "product_title": product.get('title', 'Unknown'),
                "error": defect
            })

        return defects

    def run_tests(self) -> Dict:
        """Run all tests and return results"""
        print("Starting API Testing for https://fakestoreapi.com/products\n")

        # Test 1: Fetch products and validate response code
        print("Test 1: Checking API response...")
        status_code, products = self.fetch_products()
        response_valid = self.validate_response_code(status_code)
        print(f"Response Code: {status_code} - {'PASS' if response_valid else 'FAIL'}\n")

        # Test 2: Validate each product
        print("Test 2: Validating product data...")
        if products:
            for index, product in enumerate(products):
                defects = self.validate_product(product, index)
                if defects:
                    print(f"Product {product.get('id', index)}: DEFECTS FOUND")
                    for defect in defects:
                        print(f"  - {defect}")
                else:
                    print(f"Product {product.get('id', index)}: OK")
        else:
            print("No products to validate")

        # Generate report
        return self.generate_report()

    def generate_report(self) -> Dict:
        """Generate a comprehensive test report"""
        report = {
            "total_products": len(self.products),
            "total_defects": len(self.defects),
            "defective_products": {},
            "summary": {
                "api_response_errors": 0,
                "missing_attributes": 0,
                "empty_values": 0,
                "invalid_values": 0
            }
        }

        # Categorize defects
        for defect in self.defects:
            if defect["type"] == "API Response Error":
                report["summary"]["api_response_errors"] += 1
            else:
                product_id = defect["product_id"]
                if product_id not in report["defective_products"]:
                    report["defective_products"][product_id] = {
                        "title": defect["product_title"],
                        "defects": []
                    }
                report["defective_products"][product_id]["defects"].append(defect["error"])

                # Categorize by error type
                error = defect["error"].lower()
                if "missing" in error:
                    report["summary"]["missing_attributes"] += 1
                elif "empty" in error:
                    report["summary"]["empty_values"] += 1
                else:
                    report["summary"]["invalid_values"] += 1

        return report

    def print_report(self, report: Dict):
        """Print a formatted test report"""
        print("\n" + "=" * 50)
        print("TEST REPORT")
        print("=" * 50)
        print(f"Total Products Tested: {report['total_products']}")
        print(f"Total Defects Found: {report['total_defects']}")
        print(f"\nDefect Summary:")
        print(f"  - API Response Errors: {report['summary']['api_response_errors']}")
        print(f"  - Missing Attributes: {report['summary']['missing_attributes']}")
        print(f"  - Empty Values: {report['summary']['empty_values']}")
        print(f"  - Invalid Values: {report['summary']['invalid_values']}")

        if report['defective_products']:
            print(f"\nDefective Products ({len(report['defective_products'])}):")
            for product_id, info in report['defective_products'].items():
                print(f"\nProduct ID: {product_id}")
                print(f"Title: {info['title']}")
                print("Defects:")
                for defect in info['defects']:
                    print(f"  - {defect}")
        else:
            print("\nNo defective products found!")

        print("\n" + "=" * 50)


def main():
    """Main function to run the API tests"""
    # Test with actual API
    print("Testing ACTUAL API...")
    validator = ProductDataValidator()
    report = validator.run_tests()
    validator.print_report(report)

    # Save detailed results to file
    with open('api_test_results.json', 'w') as f:
        json.dump({
            'report': report,
            'detailed_defects': validator.defects
        }, f, indent=2)

    print("\nDetailed results saved to 'api_test_results.json'")

    # Test with synthetic data containing defects
    print("\n\nTesting with SYNTHETIC DATA containing defects...")
    test_with_defective_data()


def test_with_defective_data():
    """Test with synthetic data containing various defects"""
    # Create synthetic defective data
    defective_products = [
        {
            "id": 101,
            "title": "",  # Empty title
            "price": 49.99,
            "category": "test",
            "rating": {"rate": 4.2, "count": 100}
        },
        {
            "id": 102,
            "title": "Product with negative price",
            "price": -19.99,  # Negative price
            "category": "test",
            "rating": {"rate": 3.5, "count": 50}
        },
        {
            "id": 103,
            "title": "Product with high rating",
            "price": 39.99,
            "category": "test",
            "rating": {"rate": 6.5, "count": 200}  # Rating exceeds 5
        },
        {
            "id": 104,
            "title": "Product missing price",
            # Missing price attribute
            "category": "test",
            "rating": {"rate": 4.0, "count": 75}
        },
        {
            "id": 105,
            "title": "Product missing rating",
            "price": 29.99,
            "category": "test"
            # Missing rating attribute
        },
        {
            "id": 106,
            # Missing title attribute
            "price": 59.99,
            "category": "test",
            "rating": {"rate": 3.8, "count": 125}
        }
    ]

    # Create validator with mock data
    validator = ProductDataValidator()
    validator.products = defective_products

    # Validate each product
    for index, product in enumerate(defective_products):
        defects = validator.validate_product(product, index)
        if defects:
            print(f"Product {product.get('id', index)}: DEFECTS FOUND")
            for defect in defects:
                print(f"  - {defect}")
        else:
            print(f"Product {product.get('id', index)}: OK")

    # Generate and print report
    report = validator.generate_report()
    validator.print_report(report)

    # Save synthetic test results
    with open('synthetic_test_results.json', 'w') as f:
        json.dump({
            'report': report,
            'detailed_defects': validator.defects,
            'test_data': defective_products
        }, f, indent=2)

    print("\nSynthetic test results saved to 'synthetic_test_results.json'")


if __name__ == "__main__":
    main()
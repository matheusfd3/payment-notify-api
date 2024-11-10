import sys
sys.path.append("../")

import pytest
import os
from payments.pix import Pix

def test_create_pix_payment():
    pix = Pix()
    payment = pix.create_payment(base_dir="../")
    
    assert "bank_payment_id" in payment
    assert "qr_code_path" in payment

    qr_code_path = payment["qr_code_path"]
    assert os.path.isfile(f"../static/qr_codes/{qr_code_path}.png") == True
import nox
from rescale.rescale import rescale
import numpy as np
from pytest import approx

# @nox.session
# def tests(session):
#     session.install("pytest")
#     session.run("pytest")

def test_rescale():
    assert rescale(np.linspace(0,100,5)) == approx(
        np.array([0.0, 0.25, 0.50, 0.75, 1.0])
    )

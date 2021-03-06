.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_geochem_scaling.py:


Unit Scaling
=============


.. code-block:: default

    import pyrolite.geochem
    import pandas as pd

    pd.set_option("precision", 3)  # smaller outputs








.. code-block:: default

    from pyrolite.util.synthetic import test_df

    df = test_df(cols=['CaO', 'MgO', 'SiO2', 'FeO', 'Ni', 'Ti', 'La', 'Lu', 'Mg/Fe'])








.. code-block:: default

    cols = ["Ni", "NiO", "La", "La2O3"]
    df.head(2).pyrochem.convert_chemistry(to=cols)[cols]  # these are in ppm!





.. only:: builder_html

    .. raw:: html

        <div>
        <style scoped>
            .dataframe tbody tr th:only-of-type {
                vertical-align: middle;
            }

            .dataframe tbody tr th {
                vertical-align: top;
            }

            .dataframe thead th {
                text-align: right;
            }
        </style>
        <table border="1" class="dataframe">
          <thead>
            <tr style="text-align: right;">
              <th></th>
              <th>Ni</th>
              <th>NiO</th>
              <th>La</th>
              <th>La2O3</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>0</td>
              <td>0.644</td>
              <td>0.820</td>
              <td>0.004</td>
              <td>0.005</td>
            </tr>
            <tr>
              <td>1</td>
              <td>0.650</td>
              <td>0.827</td>
              <td>0.004</td>
              <td>0.004</td>
            </tr>
          </tbody>
        </table>
        </div>
        <br />
        <br />


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.084 seconds)


.. _sphx_glr_download_examples_geochem_scaling.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example


  .. container:: binder-badge

    .. image:: https://mybinder.org/badge_logo.svg
      :target: https://mybinder.org/v2/gh/morganjwilliams/pyrolite/develop?filepath=docs/source/examples/geochem/scaling.ipynb
      :width: 150 px


  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: scaling.py <scaling.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: scaling.ipynb <scaling.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_

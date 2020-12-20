{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled6.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "pMPksYiUsLuj"
      },
      "source": [
        "# integration numerique par la methode des rectangles avec alpha = a\n",
        "\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "\n",
        "       \n",
        "\n",
        "\n"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "GSMpI2ABQtFc",
        "outputId": "9cb24c3c-386a-4365-859e-bb40e6ae2812"
      },
      "source": [
        "def compute_integrale_rectangle(x, y, nbi):\n",
        "    \n",
        "    integrale =0.\n",
        "    for i in range(nbi):\n",
        "        integrale = integrale + y[i]*(x[i+1]-x[i])\n",
        "        \n",
        "    return integrale\n",
        "\n",
        "def plot_integrale(x, y, nbi):\n",
        "  \n",
        "    for i in range(nbi):\n",
        "        # dessin du rectangle\n",
        "        x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]] # abscisses des sommets\n",
        "        y_rect = [0   , y[i], y[i]  , 0     , 0   ] # ordonnees des sommets\n",
        "        plt.plot(x_rect, y_rect,\"r\")\n",
        "\n",
        "xmin = 0\n",
        "xmax = 3*np.pi/2\n",
        "nbx = 20\n",
        "nbi = nbx - 1 # nombre d'intervalles\n",
        "\n",
        "x = np.linspace(xmin, xmax, nbx)\n",
        "y = np.cos(x)\n",
        "plt.plot(x,y,\"bo-\")\n",
        "\n",
        "integrale = compute_integrale_rectangle(x, y, nbi)\n",
        "plot_integrale(x, y, nbi)   \n",
        "\n",
        "print(\"integrale =\", integrale)\n",
        "\n",
        "plt.show()"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "integrale = -0.8708583208502408\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KDaE3bc8QrXz"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}

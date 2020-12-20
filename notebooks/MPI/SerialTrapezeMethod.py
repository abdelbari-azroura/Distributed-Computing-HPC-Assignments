{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled7.ipynb",
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
        "id": "SrHyPF-WX759"
      },
      "source": [
        "\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EBhBnwOeYTXp"
      },
      "source": [
        "def compute_integrale_trapeze(x, y, nbi):\n",
        "\n",
        "    integrale = 0.\n",
        "    for i in range(nbi):\n",
        "        trap = (x[i+1]-x[i])/2 * (y[i]+y[i+1])\n",
        "        integrale = integrale + trap\n",
        "                \n",
        "    return integrale"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "y_ykeFaHYV7L"
      },
      "source": [
        "def plot_integrale(x, y, nbi):\n",
        "    for i in range(nbi):\n",
        "        # dessin du rectangle\n",
        "        x_trap = [x[i], x[i], x[i+1], x[i+1], x[i]] # abscisses des sommets\n",
        "        y_trap = [0   , y[i], y[i+1],      0,        0   ] # ordonnees des sommets\n",
        "        plt.plot(x_trap, y_trap,\"r\")\n",
        "    \n",
        "    return 0"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "-tyDbsaQYYvv",
        "outputId": "c01463e8-d510-45bc-b87e-b7d8367ef85a"
      },
      "source": [
        "xmin = 0\n",
        "xmax = 3*np.pi/2\n",
        "nbx = 20\n",
        "nbi = nbx - 1 # nombre d'intervalles\n",
        "\n",
        "x = np.linspace(xmin, xmax, nbx)\n",
        "y = np.cos(x)\n",
        "plt.plot(x,y,\"bo-\")\n",
        "\n",
        "\n",
        "integrale = compute_integrale_trapeze(x, y, nbi)\n",
        "plot_integrale(x, y, nbi)   \n",
        "    \n",
        "print(\"integrale =\", integrale)\n",
        "\n",
        "plt.show()"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "integrale = -0.9948685571761535\n"
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
    }
  ]
}

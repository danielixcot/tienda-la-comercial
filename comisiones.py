# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

ANCHO_REPORTE = 44
META_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
META_BONO = 50000
MONTO_BONO = 500
SIN_BONO = 0
TASA_COMISION_BASE = 0.05
DECIMALES_MONEDA = 2

# lista de vendedores
vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(ventas_mensuales):
    # si vendio mas de 30000
    if ventas_mensuales > META_COMISION_ALTA:
        # calcula la comision del 8%
        tasa_comision = TASA_COMISION_ALTA
    else:
        # calcula la comision del 5%
        tasa_comision = TASA_COMISION_BASE

    return round(
        ventas_mensuales * tasa_comision,
        DECIMALES_MONEDA
    )


def calcular_bono(ventas_mensuales):
    # el bono es de 300
    if ventas_mensuales > META_BONO:
        return MONTO_BONO

    return SIN_BONO


def calcular_pago_vendedor(ventas_mensuales):
    comision = calcular_comision(ventas_mensuales)
    bono = calcular_bono(ventas_mensuales)

    return round(
        comision + bono,
        DECIMALES_MONEDA
    )


def calcular_pagos():
    pagos_vendedores = []
    total_pagar = 0

    # recorre la lista
    for nombre_vendedor, ventas_mensuales in vendedores:
        total_vendedor = calcular_pago_vendedor(ventas_mensuales)

        pagos_vendedores.append(
            (nombre_vendedor, total_vendedor)
        )

        total_pagar = total_pagar + total_vendedor

    return pagos_vendedores, total_pagar


def imprimir_reporte(pagos_vendedores, total_pagar):
    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, total_vendedor in pagos_vendedores:
        print(
            nombre_vendedor
            + ": Q "
            + str(total_vendedor)
        )

    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * ANCHO_REPORTE)
    print(
        "Total a pagar: Q "
        + str(round(total_pagar, DECIMALES_MONEDA))
    )


def generar_reporte_comisiones():
    pagos_vendedores, total_pagar = calcular_pagos()
    imprimir_reporte(pagos_vendedores, total_pagar)


generar_reporte_comisiones()
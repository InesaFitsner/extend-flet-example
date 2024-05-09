import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

class SpinkitControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const SpinkitControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    var color = control.attrColor("color", context);
    var size = control.attrDouble("size");

    return constrainedControl(
        context,
        SpinKitRotatingCircle(
          color: color,
          size: size ?? 50,
        ),
        parent,
        control);
  }
}

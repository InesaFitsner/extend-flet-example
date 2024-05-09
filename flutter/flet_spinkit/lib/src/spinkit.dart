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
    return constrainedControl(
        context,
        const SpinKitRotatingCircle(
          color: Colors.green,
          size: 100.0,
        ),
        parent,
        control);
  }
}

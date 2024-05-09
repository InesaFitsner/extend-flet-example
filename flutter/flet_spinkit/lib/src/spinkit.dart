import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

class SpinkitControl extends StatelessWidget {
  const SpinkitControl({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return const SpinKitRotatingCircle(
      color: Colors.amber,
      size: 100.0,
    );
  }
}

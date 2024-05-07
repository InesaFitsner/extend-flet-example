//library flet_spinkit;

import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

// import '../models/control.dart';
// import '../utils/alignment.dart';
// import '../utils/edge_insets.dart';
// import '../utils/text.dart';
// import '../utils/transforms.dart';
// import 'create_control.dart';

class SpinkitControl extends StatelessWidget {
  // final Control? parent;
  final Control control;
  // final List<Control> children;
  // final bool parentDisabled;
  // final bool? parentAdaptive;

  const SpinkitControl({
    super.key,
    // required this.parent,
    required this.control,
    // required this.children,
    // required this.parentDisabled,
    // required this.parentAdaptive,
  });

  @override
  Widget build(BuildContext context) {
    //debugPrint("Spinkit build: ${control.id}");

    //var color = control.attrColor("color", context);
    var color = Colors.green;

    return SpinKitRotatingCircle(
      color: color,
      size: 100.0,
    );
  }
}

// import 'package:flutter/material.dart';
// import 'package:flutter_spinkit/flutter_spinkit.dart';

// class FletCard extends StatelessWidget {
//   const FletCard({super.key});
//   var color = control.attrColor("bgcolor", context);

//   @override
//   Widget build(BuildContext context) {
//     return const SpinKitRotatingCircle(
//       color: Colors.blue,
//       size: 100.0,
//     );
//   }
// }

import 'package:flet/flet.dart';

import 'spinkit.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "spinkit":
      return const SpinkitControl();
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}

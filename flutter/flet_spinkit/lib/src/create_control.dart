import 'package:flet/flet.dart';

import 'spinkit.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "spinkit":
      return SpinkitControl(
        // parent: args.parent,
        control: args.control,
        // nextChild: args.nextChild,
        // backend: args.backend
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}

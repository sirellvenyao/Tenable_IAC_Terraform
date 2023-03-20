mock "tfconfig" {
  module {
    source = "mock-tfconfig.sentinel"
  }
}

mock "tfconfig/v1" {
  module {
    source = "mock-tfconfig.sentinel"
  }
}

mock "tfconfig/v2" {
  module {
    source = "mock-tfconfig-v2.sentinel"
  }
}

mock "tfplan" {
  module {
    source = "mock-tfplan.sentinel"
  }
}

mock "tfplan/v1" {
  module {
    source = "mock-tfplan.sentinel"
  }
}

mock "tfplan/v2" {
  module {
    source = "mock-tfplan-v2.sentinel"
  }
}

mock "tfstate" {
  module {
    source = "mock-tfstate.sentinel"
  }
}

mock "tfstate/v1" {
  module {
    source = "mock-tfstate.sentinel"
  }
}

mock "tfstate/v2" {
  module {
    source = "mock-tfstate-v2.sentinel"
  }
}

mock "tfrun" {
  module {
    source = "mock-tfrun.sentinel"
  }
}

module "tfplan-functions" {
  source = "../common-functions/tfplan-functions/tfplan-functions.sentinel"
}

module "tfstate-functions" {
  source = "../common-functions/tfstate-functions/tfstate-functions.sentinel"
}

module "tfconfig-functions" {
  source = "../common-functions/tfconfig-functions/tfconfig-functions.sentinel"
}


module "aws-functions" {
  source = "./aws-functions/aws-functions.sentinel"
}
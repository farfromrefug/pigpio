{
  "target_name": "<(module_name)",
  "targets": [{
    "target_name": "pigpio",
    "conditions": [[
      "OS == \"linux\"", {
        "cflags": [
          "-Wno-unused-local-typedefs"
        ]
      }]
    ],
    "include_dirs" : [
      "<!(node -e \"require('nan')\")"
    ],
    "sources": [
      "./src/pigpio.cc"
    ],
    "link_settings": {
      "libraries": [
        "-lpigpio"
      ]
    }
  },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
      {
        "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
        "destination": "<(module_path)"
      }
      ]
    }]
}


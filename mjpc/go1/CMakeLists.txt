# Copy the model files to the binary directory to make them available to the
# built binary.

# Start by pulling the Go1 model from MuJoCo Menagerie
add_custom_target(
  copy_menagerie_go1_resources ALL
  COMMAND ${CMAKE_COMMAND} -E copy_directory
          ${menagerie_SOURCE_DIR}/unitree_go1/assets
          ${CMAKE_CURRENT_BINARY_DIR}/go1/assets
  COMMENT "Copying Unitree Go1 from MuJoCo Menagerie")

# Add further task XML from this repository
add_custom_target(copy_go1_resources ALL
COMMAND ${CMAKE_COMMAND} -E copy
${CMAKE_CURRENT_SOURCE_DIR}/task_flat.xml
${CMAKE_CURRENT_SOURCE_DIR}/task_hill.xml
${CMAKE_CURRENT_SOURCE_DIR}/go1.xml
${CMAKE_CURRENT_BINARY_DIR}
COMMENT "Copying Go1 task XML into binary directory")

add_dependencies(copy_go1_resources copy_menagerie_go1_resources)

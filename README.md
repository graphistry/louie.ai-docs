# Welcome to Louie: Admin Guide

Louie.AI is the first genAI-native investigation platform. It supports both cloud and on-prem deployment options.

For detailed documentation, please visit [Louie Admin Docs](https://louie-admin-docs.readthedocs.io/en/latest/).

```
louie.ai-docs
├─ .DS_Store
├─ CHANGELOG.md
├─ LICENSE
├─ README.md
├─ _build
│  ├─ .DS_Store
│  └─ html
│     ├─ .buildinfo
│     ├─ 001_Meet_Louie.html
│     ├─ 003_Distributions.html
│     ├─ 004_Network_Architecture.html
│     ├─ 005_Container_Architecture.html
│     ├─ 006_System_Requirements.html
│     ├─ 007_LLM_Support.html
│     ├─ 008_LLM_Configuration.html
│     ├─ 009_AWS_Requirements.html
│     ├─ 010_Logon_and_Services.html
│     ├─ 011_Authentication_Registration.html
│     ├─ 015_JWT_Refresh.html
│     ├─ 020_Database_Config.html
│     ├─ 025_GIS_Mapping.html
│     ├─ 026_Python_Package_Config.html
│     ├─ 027_Backups.html
│     ├─ 028_Security.html
│     ├─ 029_LLM_Authorization.html
│     ├─ 030_Security_Decisions.html
│     ├─ 031_Sandbox_Network_Architecture.html
│     ├─ 032_Security_APIs.html
│     ├─ _images
│     │  ├─ Louie_Network_Architecture.png
│     │  └─ Louie_logo.png
│     ├─ _sources
│     │  ├─ 001_Meet_Louie.md.txt
│     │  ├─ 003_Distributions.md.txt
│     │  ├─ 004_Network_Architecture.md.txt
│     │  ├─ 005_Container_Architecture.md.txt
│     │  ├─ 006_System_Requirements.md.txt
│     │  ├─ 007_LLM_Support.md.txt
│     │  ├─ 008_LLM_Configuration.md.txt
│     │  ├─ 009_AWS_Requirements.md.txt
│     │  ├─ 010_Logon_and_Services.md.txt
│     │  ├─ 011_Authentication_Registration.md.txt
│     │  ├─ 015_JWT_Refresh.md.txt
│     │  ├─ 020_Database_Config.md.txt
│     │  ├─ 025_GIS_Mapping.md.txt
│     │  ├─ 026_Python_Package_Config.md.txt
│     │  ├─ 027_Backups.md.txt
│     │  ├─ 028_Security.md.txt
│     │  ├─ 029_LLM_Authorization.md.txt
│     │  ├─ 030_Security_Decisions.md.txt
│     │  ├─ 031_Sandbox_Network_Architecture.md.txt
│     │  ├─ 032_Security_APIs.md.txt
│     │  ├─ admin
│     │  │  ├─ 001_Meet_Louie.md.txt
│     │  │  ├─ 003_Distributions.md.txt
│     │  │  ├─ 004_Network_Architecture.md.txt
│     │  │  ├─ 005_Container_Architecture.md.txt
│     │  │  ├─ 006_System_Requirements.md.txt
│     │  │  ├─ 007_LLM_Support.md.txt
│     │  │  ├─ 008_LLM_Configuration.md.txt
│     │  │  ├─ 009_AWS_Requirements.md.txt
│     │  │  ├─ 010_Logon_and_Services.md.txt
│     │  │  ├─ 011_Authentication_Registration.md.txt
│     │  │  ├─ 015_JWT_Refresh.md.txt
│     │  │  ├─ 020_Database_Config.md.txt
│     │  │  ├─ 025_GIS_Mapping.md.txt
│     │  │  ├─ 026_Python_Package_Config.md.txt
│     │  │  ├─ 027_Backups.md.txt
│     │  │  ├─ 028_Security.md.txt
│     │  │  ├─ 029_LLM_Authorization.md.txt
│     │  │  ├─ 030_Security_Decisions.md.txt
│     │  │  ├─ 031_Sandbox_Network_Architecture.md.txt
│     │  │  ├─ 032_Security_APIs.md.txt
│     │  │  ├─ configuration.rst.txt
│     │  │  ├─ deployment.rst.txt
│     │  │  ├─ introduction.rst.txt
│     │  │  ├─ maintenance.rst.txt
│     │  │  └─ security.rst.txt
│     │  ├─ admin.rst.txt
│     │  ├─ configuration.rst.txt
│     │  ├─ deployment.rst.txt
│     │  ├─ index.rst.txt
│     │  ├─ introduction.rst.txt
│     │  ├─ maintenance.rst.txt
│     │  ├─ security.rst.txt
│     │  ├─ user
│     │  │  ├─ 010_.md.txt
│     │  │  ├─ 011_Thread.md.txt
│     │  │  ├─ 012_Blocks.md.txt
│     │  │  ├─ 013_Add_block.md.txt
│     │  │  ├─ 014_.md.txt
│     │  │  ├─ 015_.md.txt
│     │  │  ├─ 016_.md.txt
│     │  │  ├─ 017_.md.txt
│     │  │  ├─ 018_.md.txt
│     │  │  ├─ 019_Python.md.txt
│     │  │  ├─ 01_Meet_L_O_U_I_E_.md.txt
│     │  │  ├─ 020_Python_AI.md.txt
│     │  │  ├─ 021_Run.md.txt
│     │  │  ├─ 022_Python_data_flow.md.txt
│     │  │  ├─ 023_Python_Maps.md.txt
│     │  │  ├─ 024_Python_Outputs.md.txt
│     │  │  ├─ 025_Python_AI.md.txt
│     │  │  ├─ 026_Dashboards.md.txt
│     │  │  ├─ 027_Notebook_vs_Dashboard_Tabs.md.txt
│     │  │  ├─ 028_Add___Edit_Panels.md.txt
│     │  │  ├─ 029_Responsive_Panel_Layouts.md.txt
│     │  │  ├─ 02_Louie_AI_UI_Guide__Table_of_contents.md.txt
│     │  │  ├─ 030_Cross_Filtering.md.txt
│     │  │  ├─ 031_Input_Groups.md.txt
│     │  │  ├─ 032_Refresh_Data.md.txt
│     │  │  ├─ 033_Chart_authoring.md.txt
│     │  │  ├─ 034_Many_visualization_types_natively_supported.md.txt
│     │  │  ├─ 035_Chart_AI.md.txt
│     │  │  ├─ 036_Chart_passthrough.md.txt
│     │  │  ├─ 037_Perspective_charts.md.txt
│     │  │  ├─ 038_Perspective__Data_download.md.txt
│     │  │  ├─ 039_Perspective__Chart_switching.md.txt
│     │  │  ├─ 03_Overview.md.txt
│     │  │  ├─ 040_.md.txt
│     │  │  ├─ 041_Perspective__Expressions___Group_By.md.txt
│     │  │  ├─ 042_Perspective__Expressions___Split_By.md.txt
│     │  │  ├─ 043_Perspective__Expressions___Order_By.md.txt
│     │  │  ├─ 044_Perspective__Chart___Datagrid.md.txt
│     │  │  ├─ 045_Perspective__Chart___Y_Bar.md.txt
│     │  │  ├─ 046_Perspective__Chart___X_Bar.md.txt
│     │  │  ├─ 047_Perspective__Chart___X_Y_Bar.md.txt
│     │  │  ├─ 048_Perspective__Chart___Heatmap.md.txt
│     │  │  ├─ 049_Perspective__Chart___Y_Area.md.txt
│     │  │  ├─ 04____.md.txt
│     │  │  ├─ 050_Perspective__Chart___Y_Line.md.txt
│     │  │  ├─ 051_Large_charts.md.txt
│     │  │  ├─ 052_Large_charts__General.md.txt
│     │  │  ├─ 053_Large_charts__Specific_charts.md.txt
│     │  │  ├─ 054_Learning_Louie.md.txt
│     │  │  ├─ 055_Louie_uses_and_learns_AI_knowledge_bases.md.txt
│     │  │  ├─ 056_System_level__For_all_users__only_admin_editable.md.txt
│     │  │  ├─ 057_Recipes.md.txt
│     │  │  ├─ 058_Database_tools.md.txt
│     │  │  ├─ 059_.md.txt
│     │  │  ├─ 05____.md.txt
│     │  │  ├─ 060_.md.txt
│     │  │  ├─ 061_.md.txt
│     │  │  ├─ 062_.md.txt
│     │  │  ├─ 063_.md.txt
│     │  │  ├─ 064_Guard_rails.md.txt
│     │  │  ├─ 065_Administrators_can_set_guard_rail_prompts_on_all_or_specific_AI_tools.md.txt
│     │  │  ├─ 066_API.md.txt
│     │  │  ├─ 067_Louie_API_for_conversational_analytics__Embedding__headless___.md.txt
│     │  │  ├─ 068_Additional_features___contact_dedicated_support_staff_for_more_information_.md.txt
│     │  │  ├─ 06_Documents__comms___.md.txt
│     │  │  ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI.md.txt
│     │  │  ├─ 08_Main_area___threads.md.txt
│     │  │  └─ 09_Main_areas.md.txt
│     │  └─ user.rst.txt
│     ├─ _static
│     │  ├─ basic.css
│     │  ├─ check-solid.svg
│     │  ├─ clipboard.min.js
│     │  ├─ copy-button.svg
│     │  ├─ copybutton.css
│     │  ├─ copybutton.js
│     │  ├─ copybutton_funcs.js
│     │  ├─ doctools.js
│     │  ├─ documentation_options.js
│     │  ├─ favicon.ico
│     │  ├─ file.png
│     │  ├─ graphistry.css
│     │  ├─ graphistry_banner_transparent_colored.png
│     │  ├─ images
│     │  │  └─ user
│     │  │     ├─ 010__1.png
│     │  │     ├─ 011_Thread_1.png
│     │  │     ├─ 013_Add_block_1.png
│     │  │     ├─ 013_Add_block_2.png
│     │  │     ├─ 014__1.png
│     │  │     ├─ 014__2.png
│     │  │     ├─ 015__1.png
│     │  │     ├─ 015__2.png
│     │  │     ├─ 015__3.png
│     │  │     ├─ 016__1.png
│     │  │     ├─ 017__1.png
│     │  │     ├─ 017__2.png
│     │  │     ├─ 017__3.png
│     │  │     ├─ 018__1.png
│     │  │     ├─ 018__2.png
│     │  │     ├─ 01_Meet_L_O_U_I_E__1.png
│     │  │     ├─ 020_Python_AI_1.png
│     │  │     ├─ 020_Python_AI_2.png
│     │  │     ├─ 021_Run_1.png
│     │  │     ├─ 021_Run_2.png
│     │  │     ├─ 022_Python_data_flow_1.png
│     │  │     ├─ 022_Python_data_flow_2.png
│     │  │     ├─ 022_Python_data_flow_3.png
│     │  │     ├─ 023_Python_Maps_1.png
│     │  │     ├─ 023_Python_Maps_2.png
│     │  │     ├─ 023_Python_Maps_3.png
│     │  │     ├─ 023_Python_Maps_4.png
│     │  │     ├─ 024_Python_Outputs_1.png
│     │  │     ├─ 024_Python_Outputs_2.png
│     │  │     ├─ 025_Python_AI_1.png
│     │  │     ├─ 027_Notebook_vs_Dashboard_Tabs_1.png
│     │  │     ├─ 027_Notebook_vs_Dashboard_Tabs_2.png
│     │  │     ├─ 028_Add___Edit_Panels_1.png
│     │  │     ├─ 028_Add___Edit_Panels_2.png
│     │  │     ├─ 028_Add___Edit_Panels_3.png
│     │  │     ├─ 029_Responsive_Panel_Layouts_1.png
│     │  │     ├─ 029_Responsive_Panel_Layouts_2.png
│     │  │     ├─ 030_Cross_Filtering_1.png
│     │  │     ├─ 030_Cross_Filtering_2.png
│     │  │     ├─ 030_Cross_Filtering_3.png
│     │  │     ├─ 031_Input_Groups_1.png
│     │  │     ├─ 031_Input_Groups_2.png
│     │  │     ├─ 031_Input_Groups_3.png
│     │  │     ├─ 031_Input_Groups_4.png
│     │  │     ├─ 032_Refresh_Data_1.png
│     │  │     ├─ 034_Many_visualization_types_natively_supported_1.png
│     │  │     ├─ 034_Many_visualization_types_natively_supported_2.png
│     │  │     ├─ 034_Many_visualization_types_natively_supported_3.png
│     │  │     ├─ 034_Many_visualization_types_natively_supported_4.png
│     │  │     ├─ 034_Many_visualization_types_natively_supported_5.png
│     │  │     ├─ 035_Chart_AI_1.png
│     │  │     ├─ 035_Chart_AI_2.png
│     │  │     ├─ 036_Chart_passthrough_1.png
│     │  │     ├─ 036_Chart_passthrough_2.png
│     │  │     ├─ 038_Perspective__Data_download_1.png
│     │  │     ├─ 038_Perspective__Data_download_2.png
│     │  │     ├─ 038_Perspective__Data_download_3.png
│     │  │     ├─ 039_Perspective__Chart_switching_1.png
│     │  │     ├─ 039_Perspective__Chart_switching_2.png
│     │  │     ├─ 039_Perspective__Chart_switching_3.png
│     │  │     ├─ 039_Perspective__Chart_switching_4.png
│     │  │     ├─ 040__1.png
│     │  │     ├─ 041_Perspective__Expressions___Group_By_1.png
│     │  │     ├─ 042_Perspective__Expressions___Split_By_1.png
│     │  │     ├─ 043_Perspective__Expressions___Order_By_1.png
│     │  │     ├─ 044_Perspective__Chart___Datagrid_1.png
│     │  │     ├─ 044_Perspective__Chart___Datagrid_2.png
│     │  │     ├─ 045_Perspective__Chart___Y_Bar_1.png
│     │  │     ├─ 045_Perspective__Chart___Y_Bar_2.png
│     │  │     ├─ 046_Perspective__Chart___X_Bar_1.png
│     │  │     ├─ 046_Perspective__Chart___X_Bar_2.png
│     │  │     ├─ 047_Perspective__Chart___X_Y_Bar_1.png
│     │  │     ├─ 048_Perspective__Chart___Heatmap_1.png
│     │  │     ├─ 049_Perspective__Chart___Y_Area_1.png
│     │  │     ├─ 04_____1.png
│     │  │     ├─ 04_____2.png
│     │  │     ├─ 050_Perspective__Chart___Y_Line_1.png
│     │  │     ├─ 055_Louie_uses_and_learns_AI_knowledge_bases_1.png
│     │  │     ├─ 055_Louie_uses_and_learns_AI_knowledge_bases_2.png
│     │  │     ├─ 056_System_level__For_all_users__only_admin_editable_1.png
│     │  │     ├─ 057_Recipes_1.png
│     │  │     ├─ 059__1.png
│     │  │     ├─ 059__2.png
│     │  │     ├─ 059__3.png
│     │  │     ├─ 05_____1.png
│     │  │     ├─ 060__1.png
│     │  │     ├─ 060__2.png
│     │  │     ├─ 060__3.png
│     │  │     ├─ 061__1.png
│     │  │     ├─ 061__2.png
│     │  │     ├─ 061__3.png
│     │  │     ├─ 061__4.png
│     │  │     ├─ 061__5.png
│     │  │     ├─ 062__1.png
│     │  │     ├─ 062__2.png
│     │  │     ├─ 062__3.png
│     │  │     ├─ 063__1.png
│     │  │     ├─ 063__2.png
│     │  │     ├─ 067_Louie_API_for_conversational_analytics__Embedding__headless____1.png
│     │  │     ├─ 06_Documents__comms____1.png
│     │  │     ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_1.png
│     │  │     ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_2.png
│     │  │     ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_3.png
│     │  │     ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_4.png
│     │  │     ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_5.png
│     │  │     └─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_6.png
│     │  ├─ img
│     │  │  ├─ Louie
│     │  │  │  └─ Databricks_SSO_App_Connection.png
│     │  │  ├─ OIDC_setup
│     │  │  │  ├─ oidc_setup_auth0_1_1.png
│     │  │  │  ├─ oidc_setup_auth0_1_2.png
│     │  │  │  ├─ oidc_setup_auth0_1_3.png
│     │  │  │  ├─ oidc_setup_auth0_1_4.png
│     │  │  │  ├─ oidc_setup_auth0_1_5.png
│     │  │  │  ├─ oidc_setup_auth0_1_6.png
│     │  │  │  ├─ oidc_setup_auth0_1_7.png
│     │  │  │  ├─ oidc_setup_auth0_1_8.png
│     │  │  │  ├─ oidc_setup_auth0_2_1.png
│     │  │  │  ├─ oidc_setup_auth0_2_2.png
│     │  │  │  ├─ oidc_setup_auth0_3_1.png
│     │  │  │  ├─ oidc_setup_auth0_3_2.png
│     │  │  │  ├─ oidc_setup_auth0_3_3.png
│     │  │  │  ├─ oidc_setup_auth0_3_4.png
│     │  │  │  ├─ oidc_setup_auth0_3_5.png
│     │  │  │  ├─ oidc_setup_auth0_3_6.png
│     │  │  │  ├─ oidc_setup_auth0_3_7.png
│     │  │  │  ├─ oidc_setup_auth0_3_8.png
│     │  │  │  ├─ oidc_setup_graphistry_1_1.png
│     │  │  │  ├─ oidc_setup_graphistry_1_2.png
│     │  │  │  ├─ oidc_setup_graphistry_1_3.png
│     │  │  │  ├─ oidc_setup_graphistry_1_4.png
│     │  │  │  ├─ oidc_setup_graphistry_1_5.png
│     │  │  │  ├─ oidc_setup_graphistry_1_6.png
│     │  │  │  ├─ oidc_setup_graphistry_1_7.png
│     │  │  │  ├─ oidc_setup_graphistry_1_8.png
│     │  │  │  ├─ oidc_setup_keycloak_1_1.png
│     │  │  │  ├─ oidc_setup_keycloak_1_2.png
│     │  │  │  ├─ oidc_setup_keycloak_1_3.png
│     │  │  │  ├─ oidc_setup_keycloak_1_4.png
│     │  │  │  ├─ oidc_setup_keycloak_1_5.png
│     │  │  │  ├─ oidc_setup_keycloak_1_6.png
│     │  │  │  ├─ oidc_setup_keycloak_1_7.png
│     │  │  │  ├─ oidc_setup_keycloak_2_1.png
│     │  │  │  ├─ oidc_setup_keycloak_2_2.png
│     │  │  │  ├─ oidc_setup_keycloak_2_3.png
│     │  │  │  ├─ oidc_setup_okta_1_1.png
│     │  │  │  ├─ oidc_setup_okta_1_10.png
│     │  │  │  ├─ oidc_setup_okta_1_11.png
│     │  │  │  ├─ oidc_setup_okta_1_2.png
│     │  │  │  ├─ oidc_setup_okta_1_3.png
│     │  │  │  ├─ oidc_setup_okta_1_4.png
│     │  │  │  ├─ oidc_setup_okta_1_5.png
│     │  │  │  ├─ oidc_setup_okta_1_6.png
│     │  │  │  ├─ oidc_setup_okta_1_7.png
│     │  │  │  ├─ oidc_setup_okta_1_8.png
│     │  │  │  ├─ oidc_setup_okta_1_9.png
│     │  │  │  ├─ oidc_setup_okta_2_1.png
│     │  │  │  ├─ oidc_setup_okta_2_2.png
│     │  │  │  ├─ oidc_setup_okta_2_3.png
│     │  │  │  ├─ oidc_setup_okta_3_1.png
│     │  │  │  ├─ oidc_setup_okta_3_2.png
│     │  │  │  ├─ oidc_setup_okta_3_3.png
│     │  │  │  ├─ oidc_setup_okta_3_4.png
│     │  │  │  └─ oidc_setup_okta_3_5.png
│     │  │  ├─ add_user.png
│     │  │  ├─ admin.png
│     │  │  ├─ cfg_users.png
│     │  │  ├─ grafana-import-dcgm-dashboard-6.png
│     │  │  ├─ jaeger-inspecting-trace-with-error.png
│     │  │  ├─ jaeger-trace-list-including-trace-with-error.png
│     │  │  ├─ prometheus-forge-etl-python-metric-example.png
│     │  │  ├─ set_creds.png
│     │  │  ├─ set_roles.png
│     │  │  └─ signup.png
│     │  ├─ language_data.js
│     │  ├─ louie-logo-dark.png
│     │  ├─ louie-logo.png
│     │  ├─ minus.png
│     │  ├─ nbsphinx-broken-thumbnail.svg
│     │  ├─ nbsphinx-code-cells.css
│     │  ├─ nbsphinx-gallery.css
│     │  ├─ nbsphinx-no-thumbnail.svg
│     │  ├─ plus.png
│     │  ├─ pygments.css
│     │  ├─ scripts
│     │  │  ├─ bootstrap.js
│     │  │  ├─ bootstrap.js.LICENSE.txt
│     │  │  ├─ bootstrap.js.map
│     │  │  ├─ fontawesome.js
│     │  │  ├─ fontawesome.js.LICENSE.txt
│     │  │  ├─ fontawesome.js.map
│     │  │  ├─ pydata-sphinx-theme.js
│     │  │  └─ pydata-sphinx-theme.js.map
│     │  ├─ searchtools.js
│     │  ├─ sphinx_highlight.js
│     │  ├─ styles
│     │  │  ├─ pydata-sphinx-theme.css
│     │  │  ├─ pydata-sphinx-theme.css.map
│     │  │  └─ theme.css
│     │  ├─ vendor
│     │  │  └─ fontawesome
│     │  │     └─ webfonts
│     │  │        ├─ fa-brands-400.ttf
│     │  │        ├─ fa-brands-400.woff2
│     │  │        ├─ fa-regular-400.ttf
│     │  │        ├─ fa-regular-400.woff2
│     │  │        ├─ fa-solid-900.ttf
│     │  │        └─ fa-solid-900.woff2
│     │  └─ webpack-macros.html
│     ├─ admin
│     │  ├─ 001_Meet_Louie.html
│     │  ├─ 003_Distributions.html
│     │  ├─ 004_Network_Architecture.html
│     │  ├─ 005_Container_Architecture.html
│     │  ├─ 006_System_Requirements.html
│     │  ├─ 007_LLM_Support.html
│     │  ├─ 008_LLM_Configuration.html
│     │  ├─ 009_AWS_Requirements.html
│     │  ├─ 010_Logon_and_Services.html
│     │  ├─ 011_Authentication_Registration.html
│     │  ├─ 015_JWT_Refresh.html
│     │  ├─ 020_Database_Config.html
│     │  ├─ 025_GIS_Mapping.html
│     │  ├─ 026_Python_Package_Config.html
│     │  ├─ 027_Backups.html
│     │  ├─ 028_Security.html
│     │  ├─ 029_LLM_Authorization.html
│     │  ├─ 030_Security_Decisions.html
│     │  ├─ 031_Sandbox_Network_Architecture.html
│     │  ├─ 032_Security_APIs.html
│     │  ├─ configuration.html
│     │  ├─ deployment.html
│     │  ├─ introduction.html
│     │  ├─ maintenance.html
│     │  └─ security.html
│     ├─ admin.html
│     ├─ configuration.html
│     ├─ deployment.html
│     ├─ genindex.html
│     ├─ index.html
│     ├─ introduction.html
│     ├─ maintenance.html
│     ├─ objects.inv
│     ├─ search.html
│     ├─ searchindex.js
│     ├─ security.html
│     ├─ user
│     │  ├─ 010_.html
│     │  ├─ 011_Thread.html
│     │  ├─ 012_Blocks.html
│     │  ├─ 013_Add_block.html
│     │  ├─ 014_.html
│     │  ├─ 015_.html
│     │  ├─ 016_.html
│     │  ├─ 017_.html
│     │  ├─ 018_.html
│     │  ├─ 019_Python.html
│     │  ├─ 01_Meet_L_O_U_I_E_.html
│     │  ├─ 020_Python_AI.html
│     │  ├─ 021_Run.html
│     │  ├─ 022_Python_data_flow.html
│     │  ├─ 023_Python_Maps.html
│     │  ├─ 024_Python_Outputs.html
│     │  ├─ 025_Python_AI.html
│     │  ├─ 026_Dashboards.html
│     │  ├─ 027_Notebook_vs_Dashboard_Tabs.html
│     │  ├─ 028_Add___Edit_Panels.html
│     │  ├─ 029_Responsive_Panel_Layouts.html
│     │  ├─ 02_Louie_AI_UI_Guide__Table_of_contents.html
│     │  ├─ 030_Cross_Filtering.html
│     │  ├─ 031_Input_Groups.html
│     │  ├─ 032_Refresh_Data.html
│     │  ├─ 033_Chart_authoring.html
│     │  ├─ 034_Many_visualization_types_natively_supported.html
│     │  ├─ 035_Chart_AI.html
│     │  ├─ 036_Chart_passthrough.html
│     │  ├─ 037_Perspective_charts.html
│     │  ├─ 038_Perspective__Data_download.html
│     │  ├─ 039_Perspective__Chart_switching.html
│     │  ├─ 03_Overview.html
│     │  ├─ 040_.html
│     │  ├─ 041_Perspective__Expressions___Group_By.html
│     │  ├─ 042_Perspective__Expressions___Split_By.html
│     │  ├─ 043_Perspective__Expressions___Order_By.html
│     │  ├─ 044_Perspective__Chart___Datagrid.html
│     │  ├─ 045_Perspective__Chart___Y_Bar.html
│     │  ├─ 046_Perspective__Chart___X_Bar.html
│     │  ├─ 047_Perspective__Chart___X_Y_Bar.html
│     │  ├─ 048_Perspective__Chart___Heatmap.html
│     │  ├─ 049_Perspective__Chart___Y_Area.html
│     │  ├─ 04____.html
│     │  ├─ 050_Perspective__Chart___Y_Line.html
│     │  ├─ 051_Large_charts.html
│     │  ├─ 052_Large_charts__General.html
│     │  ├─ 053_Large_charts__Specific_charts.html
│     │  ├─ 054_Learning_Louie.html
│     │  ├─ 055_Louie_uses_and_learns_AI_knowledge_bases.html
│     │  ├─ 056_System_level__For_all_users__only_admin_editable.html
│     │  ├─ 057_Recipes.html
│     │  ├─ 058_Database_tools.html
│     │  ├─ 059_.html
│     │  ├─ 05____.html
│     │  ├─ 060_.html
│     │  ├─ 061_.html
│     │  ├─ 062_.html
│     │  ├─ 063_.html
│     │  ├─ 064_Guard_rails.html
│     │  ├─ 065_Administrators_can_set_guard_rail_prompts_on_all_or_specific_AI_tools.html
│     │  ├─ 066_API.html
│     │  ├─ 067_Louie_API_for_conversational_analytics__Embedding__headless___.html
│     │  ├─ 068_Additional_features___contact_dedicated_support_staff_for_more_information_.html
│     │  ├─ 06_Documents__comms___.html
│     │  ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI.html
│     │  ├─ 08_Main_area___threads.html
│     │  └─ 09_Main_areas.html
│     └─ user.html
├─ bin
│  ├─ ci.sh
│  ├─ clean.sh
│  └─ html.sh
├─ docs
│  ├─ .DS_Store
│  └─ source
│     ├─ .DS_Store
│     ├─ admin
│     │  ├─ .DS_Store
│     │  ├─ 001_Meet_Louie.md
│     │  ├─ 003_Distributions.md
│     │  ├─ 004_Network_Architecture.md
│     │  ├─ 005_Container_Architecture.md
│     │  ├─ 006_System_Requirements.md
│     │  ├─ 007_LLM_Support.md
│     │  ├─ 008_LLM_Configuration.md
│     │  ├─ 009_AWS_Requirements.md
│     │  ├─ 010_Logon_and_Services.md
│     │  ├─ 011_Authentication_Registration.md
│     │  ├─ 015_JWT_Refresh.md
│     │  ├─ 020_Database_Config.md
│     │  ├─ 025_GIS_Mapping.md
│     │  ├─ 026_Python_Package_Config.md
│     │  ├─ 027_Backups.md
│     │  ├─ 028_Security.md
│     │  ├─ 029_LLM_Authorization.md
│     │  ├─ 030_Security_Decisions.md
│     │  ├─ 031_Sandbox_Network_Architecture.md
│     │  ├─ 032_Security_APIs.md
│     │  ├─ architecture
│     │  ├─ authentication
│     │  ├─ configuration.rst
│     │  ├─ deployment.rst
│     │  ├─ images
│     │  │  ├─ API.png
│     │  │  ├─ AWS_Marketplace.png
│     │  │  ├─ Database_Connectors.png
│     │  │  ├─ Louie_Admin_Guide.png
│     │  │  ├─ Louie_Network_Architecture.png
│     │  │  ├─ Louie_logo.png
│     │  │  ├─ OAUTH_Setup.png
│     │  │  ├─ unamed1.png
│     │  │  └─ unnamed.png
│     │  ├─ introduction.rst
│     │  ├─ maintenance.rst
│     │  └─ security.rst
│     ├─ admin.rst
│     ├─ conf.py
│     ├─ index.rst
│     ├─ static
│     │  ├─ .DS_Store
│     │  ├─ favicon.ico
│     │  ├─ graphistry.css
│     │  ├─ graphistry_banner_transparent_colored.png
│     │  ├─ img
│     │  │  ├─ Louie
│     │  │  │  └─ Databricks_SSO_App_Connection.png
│     │  │  ├─ OIDC_setup
│     │  │  │  ├─ oidc_setup_auth0_1_1.png
│     │  │  │  ├─ oidc_setup_auth0_1_2.png
│     │  │  │  ├─ oidc_setup_auth0_1_3.png
│     │  │  │  ├─ oidc_setup_auth0_1_4.png
│     │  │  │  ├─ oidc_setup_auth0_1_5.png
│     │  │  │  ├─ oidc_setup_auth0_1_6.png
│     │  │  │  ├─ oidc_setup_auth0_1_7.png
│     │  │  │  ├─ oidc_setup_auth0_1_8.png
│     │  │  │  ├─ oidc_setup_auth0_2_1.png
│     │  │  │  ├─ oidc_setup_auth0_2_2.png
│     │  │  │  ├─ oidc_setup_auth0_3_1.png
│     │  │  │  ├─ oidc_setup_auth0_3_2.png
│     │  │  │  ├─ oidc_setup_auth0_3_3.png
│     │  │  │  ├─ oidc_setup_auth0_3_4.png
│     │  │  │  ├─ oidc_setup_auth0_3_5.png
│     │  │  │  ├─ oidc_setup_auth0_3_6.png
│     │  │  │  ├─ oidc_setup_auth0_3_7.png
│     │  │  │  ├─ oidc_setup_auth0_3_8.png
│     │  │  │  ├─ oidc_setup_graphistry_1_1.png
│     │  │  │  ├─ oidc_setup_graphistry_1_2.png
│     │  │  │  ├─ oidc_setup_graphistry_1_3.png
│     │  │  │  ├─ oidc_setup_graphistry_1_4.png
│     │  │  │  ├─ oidc_setup_graphistry_1_5.png
│     │  │  │  ├─ oidc_setup_graphistry_1_6.png
│     │  │  │  ├─ oidc_setup_graphistry_1_7.png
│     │  │  │  ├─ oidc_setup_graphistry_1_8.png
│     │  │  │  ├─ oidc_setup_keycloak_1_1.png
│     │  │  │  ├─ oidc_setup_keycloak_1_2.png
│     │  │  │  ├─ oidc_setup_keycloak_1_3.png
│     │  │  │  ├─ oidc_setup_keycloak_1_4.png
│     │  │  │  ├─ oidc_setup_keycloak_1_5.png
│     │  │  │  ├─ oidc_setup_keycloak_1_6.png
│     │  │  │  ├─ oidc_setup_keycloak_1_7.png
│     │  │  │  ├─ oidc_setup_keycloak_2_1.png
│     │  │  │  ├─ oidc_setup_keycloak_2_2.png
│     │  │  │  ├─ oidc_setup_keycloak_2_3.png
│     │  │  │  ├─ oidc_setup_okta_1_1.png
│     │  │  │  ├─ oidc_setup_okta_1_10.png
│     │  │  │  ├─ oidc_setup_okta_1_11.png
│     │  │  │  ├─ oidc_setup_okta_1_2.png
│     │  │  │  ├─ oidc_setup_okta_1_3.png
│     │  │  │  ├─ oidc_setup_okta_1_4.png
│     │  │  │  ├─ oidc_setup_okta_1_5.png
│     │  │  │  ├─ oidc_setup_okta_1_6.png
│     │  │  │  ├─ oidc_setup_okta_1_7.png
│     │  │  │  ├─ oidc_setup_okta_1_8.png
│     │  │  │  ├─ oidc_setup_okta_1_9.png
│     │  │  │  ├─ oidc_setup_okta_2_1.png
│     │  │  │  ├─ oidc_setup_okta_2_2.png
│     │  │  │  ├─ oidc_setup_okta_2_3.png
│     │  │  │  ├─ oidc_setup_okta_3_1.png
│     │  │  │  ├─ oidc_setup_okta_3_2.png
│     │  │  │  ├─ oidc_setup_okta_3_3.png
│     │  │  │  ├─ oidc_setup_okta_3_4.png
│     │  │  │  └─ oidc_setup_okta_3_5.png
│     │  │  ├─ add_user.png
│     │  │  ├─ admin.png
│     │  │  ├─ cfg_users.png
│     │  │  ├─ grafana-import-dcgm-dashboard-6.png
│     │  │  ├─ jaeger-inspecting-trace-with-error.png
│     │  │  ├─ jaeger-trace-list-including-trace-with-error.png
│     │  │  ├─ prometheus-forge-etl-python-metric-example.png
│     │  │  ├─ set_creds.png
│     │  │  ├─ set_roles.png
│     │  │  └─ signup.png
│     │  ├─ louie-logo-dark.png
│     │  └─ louie-logo.png
│     ├─ user
│     │  ├─ 010_.md
│     │  ├─ 011_Thread.md
│     │  ├─ 012_Blocks.md
│     │  ├─ 013_Add_block.md
│     │  ├─ 014_.md
│     │  ├─ 015_.md
│     │  ├─ 016_.md
│     │  ├─ 017_.md
│     │  ├─ 018_.md
│     │  ├─ 019_Python.md
│     │  ├─ 01_Meet_L_O_U_I_E_.md
│     │  ├─ 020_Python_AI.md
│     │  ├─ 021_Run.md
│     │  ├─ 022_Python_data_flow.md
│     │  ├─ 023_Python_Maps.md
│     │  ├─ 024_Python_Outputs.md
│     │  ├─ 025_Python_AI.md
│     │  ├─ 026_Dashboards.md
│     │  ├─ 027_Notebook_vs_Dashboard_Tabs.md
│     │  ├─ 028_Add___Edit_Panels.md
│     │  ├─ 029_Responsive_Panel_Layouts.md
│     │  ├─ 02_Louie_AI_UI_Guide__Table_of_contents.md
│     │  ├─ 030_Cross_Filtering.md
│     │  ├─ 031_Input_Groups.md
│     │  ├─ 032_Refresh_Data.md
│     │  ├─ 033_Chart_authoring.md
│     │  ├─ 034_Many_visualization_types_natively_supported.md
│     │  ├─ 035_Chart_AI.md
│     │  ├─ 036_Chart_passthrough.md
│     │  ├─ 037_Perspective_charts.md
│     │  ├─ 038_Perspective__Data_download.md
│     │  ├─ 039_Perspective__Chart_switching.md
│     │  ├─ 03_Overview.md
│     │  ├─ 040_.md
│     │  ├─ 041_Perspective__Expressions___Group_By.md
│     │  ├─ 042_Perspective__Expressions___Split_By.md
│     │  ├─ 043_Perspective__Expressions___Order_By.md
│     │  ├─ 044_Perspective__Chart___Datagrid.md
│     │  ├─ 045_Perspective__Chart___Y_Bar.md
│     │  ├─ 046_Perspective__Chart___X_Bar.md
│     │  ├─ 047_Perspective__Chart___X_Y_Bar.md
│     │  ├─ 048_Perspective__Chart___Heatmap.md
│     │  ├─ 049_Perspective__Chart___Y_Area.md
│     │  ├─ 04____.md
│     │  ├─ 050_Perspective__Chart___Y_Line.md
│     │  ├─ 051_Large_charts.md
│     │  ├─ 052_Large_charts__General.md
│     │  ├─ 053_Large_charts__Specific_charts.md
│     │  ├─ 054_Learning_Louie.md
│     │  ├─ 055_Louie_uses_and_learns_AI_knowledge_bases.md
│     │  ├─ 056_System_level__For_all_users__only_admin_editable.md
│     │  ├─ 057_Recipes.md
│     │  ├─ 058_Database_tools.md
│     │  ├─ 059_.md
│     │  ├─ 05____.md
│     │  ├─ 060_.md
│     │  ├─ 061_.md
│     │  ├─ 062_.md
│     │  ├─ 063_.md
│     │  ├─ 064_Guard_rails.md
│     │  ├─ 065_Administrators_can_set_guard_rail_prompts_on_all_or_specific_AI_tools.md
│     │  ├─ 066_API.md
│     │  ├─ 067_Louie_API_for_conversational_analytics__Embedding__headless___.md
│     │  ├─ 068_Additional_features___contact_dedicated_support_staff_for_more_information_.md
│     │  ├─ 06_Documents__comms___.md
│     │  ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI.md
│     │  ├─ 08_Main_area___threads.md
│     │  ├─ 09_Main_areas.md
│     │  └─ images
│     │     ├─ .DS_Store
│     │     └─ user
│     │        ├─ 010__1.png
│     │        ├─ 011_Thread_1.png
│     │        ├─ 013_Add_block_1.png
│     │        ├─ 013_Add_block_2.png
│     │        ├─ 014__1.png
│     │        ├─ 014__2.png
│     │        ├─ 015__1.png
│     │        ├─ 015__2.png
│     │        ├─ 015__3.png
│     │        ├─ 016__1.png
│     │        ├─ 017__1.png
│     │        ├─ 017__2.png
│     │        ├─ 017__3.png
│     │        ├─ 018__1.png
│     │        ├─ 018__2.png
│     │        ├─ 01_Meet_L_O_U_I_E__1.png
│     │        ├─ 020_Python_AI_1.png
│     │        ├─ 020_Python_AI_2.png
│     │        ├─ 021_Run_1.png
│     │        ├─ 021_Run_2.png
│     │        ├─ 022_Python_data_flow_1.png
│     │        ├─ 022_Python_data_flow_2.png
│     │        ├─ 022_Python_data_flow_3.png
│     │        ├─ 023_Python_Maps_1.png
│     │        ├─ 023_Python_Maps_2.png
│     │        ├─ 023_Python_Maps_3.png
│     │        ├─ 023_Python_Maps_4.png
│     │        ├─ 024_Python_Outputs_1.png
│     │        ├─ 024_Python_Outputs_2.png
│     │        ├─ 025_Python_AI_1.png
│     │        ├─ 027_Notebook_vs_Dashboard_Tabs_1.png
│     │        ├─ 027_Notebook_vs_Dashboard_Tabs_2.png
│     │        ├─ 028_Add___Edit_Panels_1.png
│     │        ├─ 028_Add___Edit_Panels_2.png
│     │        ├─ 028_Add___Edit_Panels_3.png
│     │        ├─ 029_Responsive_Panel_Layouts_1.png
│     │        ├─ 029_Responsive_Panel_Layouts_2.png
│     │        ├─ 030_Cross_Filtering_1.png
│     │        ├─ 030_Cross_Filtering_2.png
│     │        ├─ 030_Cross_Filtering_3.png
│     │        ├─ 031_Input_Groups_1.png
│     │        ├─ 031_Input_Groups_2.png
│     │        ├─ 031_Input_Groups_3.png
│     │        ├─ 031_Input_Groups_4.png
│     │        ├─ 032_Refresh_Data_1.png
│     │        ├─ 034_Many_visualization_types_natively_supported_1.png
│     │        ├─ 034_Many_visualization_types_natively_supported_2.png
│     │        ├─ 034_Many_visualization_types_natively_supported_3.png
│     │        ├─ 034_Many_visualization_types_natively_supported_4.png
│     │        ├─ 034_Many_visualization_types_natively_supported_5.png
│     │        ├─ 035_Chart_AI_1.png
│     │        ├─ 035_Chart_AI_2.png
│     │        ├─ 036_Chart_passthrough_1.png
│     │        ├─ 036_Chart_passthrough_2.png
│     │        ├─ 038_Perspective__Data_download_1.png
│     │        ├─ 038_Perspective__Data_download_2.png
│     │        ├─ 038_Perspective__Data_download_3.png
│     │        ├─ 039_Perspective__Chart_switching_1.png
│     │        ├─ 039_Perspective__Chart_switching_2.png
│     │        ├─ 039_Perspective__Chart_switching_3.png
│     │        ├─ 039_Perspective__Chart_switching_4.png
│     │        ├─ 040__1.png
│     │        ├─ 041_Perspective__Expressions___Group_By_1.png
│     │        ├─ 042_Perspective__Expressions___Split_By_1.png
│     │        ├─ 043_Perspective__Expressions___Order_By_1.png
│     │        ├─ 044_Perspective__Chart___Datagrid_1.png
│     │        ├─ 044_Perspective__Chart___Datagrid_2.png
│     │        ├─ 045_Perspective__Chart___Y_Bar_1.png
│     │        ├─ 045_Perspective__Chart___Y_Bar_2.png
│     │        ├─ 046_Perspective__Chart___X_Bar_1.png
│     │        ├─ 046_Perspective__Chart___X_Bar_2.png
│     │        ├─ 047_Perspective__Chart___X_Y_Bar_1.png
│     │        ├─ 048_Perspective__Chart___Heatmap_1.png
│     │        ├─ 049_Perspective__Chart___Y_Area_1.png
│     │        ├─ 04_____1.png
│     │        ├─ 04_____2.png
│     │        ├─ 050_Perspective__Chart___Y_Line_1.png
│     │        ├─ 055_Louie_uses_and_learns_AI_knowledge_bases_1.png
│     │        ├─ 055_Louie_uses_and_learns_AI_knowledge_bases_2.png
│     │        ├─ 056_System_level__For_all_users__only_admin_editable_1.png
│     │        ├─ 057_Recipes_1.png
│     │        ├─ 059__1.png
│     │        ├─ 059__2.png
│     │        ├─ 059__3.png
│     │        ├─ 05_____1.png
│     │        ├─ 060__1.png
│     │        ├─ 060__2.png
│     │        ├─ 060__3.png
│     │        ├─ 061__1.png
│     │        ├─ 061__2.png
│     │        ├─ 061__3.png
│     │        ├─ 061__4.png
│     │        ├─ 061__5.png
│     │        ├─ 062__1.png
│     │        ├─ 062__2.png
│     │        ├─ 062__3.png
│     │        ├─ 063__1.png
│     │        ├─ 063__2.png
│     │        ├─ 067_Louie_API_for_conversational_analytics__Embedding__headless____1.png
│     │        ├─ 06_Documents__comms____1.png
│     │        ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_1.png
│     │        ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_2.png
│     │        ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_3.png
│     │        ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_4.png
│     │        ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_5.png
│     │        └─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI_6.png
│     └─ user.rst
├─ doctrees
│  ├─ 001_Introduction.doctree
│  ├─ 001_Meet_Louie.doctree
│  ├─ 003_Distributions.doctree
│  ├─ 004_Network_Architecture.doctree
│  ├─ 005_Container_Architecture.doctree
│  ├─ 006_System_Requirements.doctree
│  ├─ 007_LLM_Support.doctree
│  ├─ 008_LLM_Configuration.doctree
│  ├─ 009_AWS_Requirements.doctree
│  ├─ 010_Logon_and_Services.doctree
│  ├─ 011_Authentication_Registration.doctree
│  ├─ 015_JWT_Refresh.doctree
│  ├─ 020_Database_Config.doctree
│  ├─ 025_GIS_Mapping.doctree
│  ├─ 026_Python_Package_Config.doctree
│  ├─ 027_Backups.doctree
│  ├─ 028_Security.doctree
│  ├─ 029_LLM_Authorization.doctree
│  ├─ 030_Security_Decisions.doctree
│  ├─ 031_Sandbox_Network_Architecture.doctree
│  ├─ 032_Security_APIs.doctree
│  ├─ _TOC.doctree
│  ├─ admin
│  │  ├─ 001_Meet_Louie.doctree
│  │  ├─ 003_Distributions.doctree
│  │  ├─ 004_Network_Architecture.doctree
│  │  ├─ 005_Container_Architecture.doctree
│  │  ├─ 006_System_Requirements.doctree
│  │  ├─ 007_LLM_Support.doctree
│  │  ├─ 008_LLM_Configuration.doctree
│  │  ├─ 009_AWS_Requirements.doctree
│  │  ├─ 010_Logon_and_Services.doctree
│  │  ├─ 011_Authentication_Registration.doctree
│  │  ├─ 015_JWT_Refresh.doctree
│  │  ├─ 020_Database_Config.doctree
│  │  ├─ 025_GIS_Mapping.doctree
│  │  ├─ 026_Python_Package_Config.doctree
│  │  ├─ 027_Backups.doctree
│  │  ├─ 028_Security.doctree
│  │  ├─ 029_LLM_Authorization.doctree
│  │  ├─ 030_Security_Decisions.doctree
│  │  ├─ 031_Sandbox_Network_Architecture.doctree
│  │  ├─ 032_Security_APIs.doctree
│  │  ├─ configuration.doctree
│  │  ├─ deployment.doctree
│  │  ├─ index.doctree
│  │  ├─ introduction.doctree
│  │  ├─ maintenance.doctree
│  │  └─ security.doctree
│  ├─ admin.doctree
│  ├─ architecture
│  │  ├─ 004_Network_Architecture.doctree
│  │  └─ 005_Container_Architecture.doctree
│  ├─ authentication
│  │  └─ 011_Authentication_Registration.doctree
│  ├─ configuration.doctree
│  ├─ deployment.doctree
│  ├─ docs
│  │  ├─ 001_Introduction.doctree
│  │  ├─ 003_Distributions.doctree
│  │  ├─ 004_Network_Architecture.doctree
│  │  ├─ 005_Container_Architecture.doctree
│  │  ├─ 006_System_Requirements.doctree
│  │  ├─ 007_LLM_Support.doctree
│  │  ├─ 008_LLM_Configuration.doctree
│  │  ├─ 009_AWS_Requirements.doctree
│  │  ├─ 010_Logon_and_Services.doctree
│  │  ├─ 011_Authentication_Registration.doctree
│  │  ├─ 015_JWT_Refresh.doctree
│  │  ├─ 020_Database_Config.doctree
│  │  ├─ 025_GIS_Mapping.doctree
│  │  ├─ 026_Python_Package_Config.doctree
│  │  ├─ 027_Backups.doctree
│  │  ├─ 028_Security.doctree
│  │  ├─ 029_LLM_Authorization.doctree
│  │  ├─ 030_Security_Decisions.doctree
│  │  ├─ 031_Sandbox_Network_Architecture.doctree
│  │  ├─ 032_Security_APIs.doctree
│  │  └─ _TOC.doctree
│  ├─ environment.pickle
│  ├─ index.doctree
│  ├─ introduction.doctree
│  ├─ maintenance.doctree
│  ├─ nbsphinx
│  ├─ security.doctree
│  ├─ user
│  │  ├─ 010_.doctree
│  │  ├─ 011_Thread.doctree
│  │  ├─ 012_Blocks.doctree
│  │  ├─ 013_Add_block.doctree
│  │  ├─ 014_.doctree
│  │  ├─ 015_.doctree
│  │  ├─ 016_.doctree
│  │  ├─ 017_.doctree
│  │  ├─ 018_.doctree
│  │  ├─ 019_Python.doctree
│  │  ├─ 01_Meet_L_O_U_I_E_.doctree
│  │  ├─ 020_Python_AI.doctree
│  │  ├─ 021_Run.doctree
│  │  ├─ 022_Python_data_flow.doctree
│  │  ├─ 023_Python_Maps.doctree
│  │  ├─ 024_Python_Outputs.doctree
│  │  ├─ 025_Python_AI.doctree
│  │  ├─ 026_Dashboards.doctree
│  │  ├─ 027_Notebook_vs_Dashboard_Tabs.doctree
│  │  ├─ 028_Add___Edit_Panels.doctree
│  │  ├─ 029_Responsive_Panel_Layouts.doctree
│  │  ├─ 02_Louie_AI_UI_Guide__Table_of_contents.doctree
│  │  ├─ 030_Cross_Filtering.doctree
│  │  ├─ 031_Input_Groups.doctree
│  │  ├─ 032_Refresh_Data.doctree
│  │  ├─ 033_Chart_authoring.doctree
│  │  ├─ 034_Many_visualization_types_natively_supported.doctree
│  │  ├─ 035_Chart_AI.doctree
│  │  ├─ 036_Chart_passthrough.doctree
│  │  ├─ 037_Perspective_charts.doctree
│  │  ├─ 038_Perspective__Data_download.doctree
│  │  ├─ 039_Perspective__Chart_switching.doctree
│  │  ├─ 03_Overview.doctree
│  │  ├─ 040_.doctree
│  │  ├─ 041_Perspective__Expressions___Group_By.doctree
│  │  ├─ 042_Perspective__Expressions___Split_By.doctree
│  │  ├─ 043_Perspective__Expressions___Order_By.doctree
│  │  ├─ 044_Perspective__Chart___Datagrid.doctree
│  │  ├─ 045_Perspective__Chart___Y_Bar.doctree
│  │  ├─ 046_Perspective__Chart___X_Bar.doctree
│  │  ├─ 047_Perspective__Chart___X_Y_Bar.doctree
│  │  ├─ 048_Perspective__Chart___Heatmap.doctree
│  │  ├─ 049_Perspective__Chart___Y_Area.doctree
│  │  ├─ 04____.doctree
│  │  ├─ 050_Perspective__Chart___Y_Line.doctree
│  │  ├─ 051_Large_charts.doctree
│  │  ├─ 052_Large_charts__General.doctree
│  │  ├─ 053_Large_charts__Specific_charts.doctree
│  │  ├─ 054_Learning_Louie.doctree
│  │  ├─ 055_Louie_uses_and_learns_AI_knowledge_bases.doctree
│  │  ├─ 056_System_level__For_all_users__only_admin_editable.doctree
│  │  ├─ 057_Recipes.doctree
│  │  ├─ 058_Database_tools.doctree
│  │  ├─ 059_.doctree
│  │  ├─ 05____.doctree
│  │  ├─ 060_.doctree
│  │  ├─ 061_.doctree
│  │  ├─ 062_.doctree
│  │  ├─ 063_.doctree
│  │  ├─ 064_Guard_rails.doctree
│  │  ├─ 065_Administrators_can_set_guard_rail_prompts_on_all_or_specific_AI_tools.doctree
│  │  ├─ 066_API.doctree
│  │  ├─ 067_Louie_API_for_conversational_analytics__Embedding__headless___.doctree
│  │  ├─ 068_Additional_features___contact_dedicated_support_staff_for_more_information_.doctree
│  │  ├─ 06_Documents__comms___.doctree
│  │  ├─ 07_Take_steps_and_leap_out_of_the_box_or_integrate_in_house_innovations_with_genAI.doctree
│  │  ├─ 08_Main_area___threads.doctree
│  │  └─ 09_Main_areas.doctree
│  └─ user.doctree
└─ infra
   ├─ Dockerfile
   ├─ build-docs.sh
   ├─ docker-compose.yml
   ├─ requirements-python.txt
   └─ requirements-system.txt

```
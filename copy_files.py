notification_names = [
    'Number of New Result for Saved Search',
    'Saved Search has been shared with you',
    'Saved Search X has been shared with your group',
]

notification_names = [
    'search_result_number',
    'search_shared',
    'search_shared_with_group',
]

for notification_name in notification_names:

    with open(f'service_panes/{notification_name}.html', 'w') as file: 
    
        pass

    with open(f'windows/{notification_name}_window.html', 'w') as file: 
    
        pass
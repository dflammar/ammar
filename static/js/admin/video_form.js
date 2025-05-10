(function($) {
    $(document).ready(function() {
        // Get field elements
        const videoTypeField = $('#id_video_type');
        const videoFileFieldset = $('.field-video_file').closest('fieldset');
        const youtubeFieldset = $('.field-youtube_url').closest('fieldset');
        
        // Function to toggle fields based on video type
        function toggleVideoFields() {
            const videoType = videoTypeField.val();
            
            if (videoType === 'file') {
                videoFileFieldset.show();
                youtubeFieldset.hide();
            } else if (videoType === 'youtube') {
                videoFileFieldset.hide();
                youtubeFieldset.show();
            }
        }
        
        // Initial toggle
        toggleVideoFields();
        
        // Toggle on change
        videoTypeField.on('change', toggleVideoFields);
        
        // Add YouTube preview when URL is entered
        const youtubeUrlField = $('#id_youtube_url');
        const previewContainer = $('<div id="youtube-preview-container" style="margin-top: 10px;"></div>');
        
        youtubeUrlField.after(previewContainer);
        
        youtubeUrlField.on('input', function() {
            const url = $(this).val();
            let videoId = '';
            
            // Extract video ID from various URL formats
            const patterns = [
                /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\?\/]+)/,
                /youtube\.com\/watch\?.*v=([^&\?\/]+)/,
                /youtube\.com\/shorts\/([^&\?\/]+)/
            ];
            
            for (const pattern of patterns) {
                const match = url.match(pattern);
                if (match) {
                    videoId = match[1];
                    break;
                }
            }
            
            if (videoId) {
                // Show preview
                previewContainer.html(`
                    <div style="margin-bottom: 10px;">
                        <strong>معاينة الفيديو:</strong>
                    </div>
                    <div style="position: relative; width: 100%; max-width: 400px;">
                        <a href="https://www.youtube.com/watch?v=${videoId}" target="_blank">
                            <img src="https://img.youtube.com/vi/${videoId}/0.jpg" 
                                 style="width: 100%; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);" />
                            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
                                <svg width="68" height="48" viewBox="0 0 68 48">
                                    <path class="ytp-large-play-button-bg" d="M66.52,7.74c-0.78-2.93-2.49-5.41-5.42-6.19C55.79,.13,34,0,34,0S12.21,.13,6.9,1.55 C3.97,2.33,2.27,4.81,1.48,7.74C0.06,13.05,0,24,0,24s0.06,10.95,1.48,16.26c0.78,2.93,2.49,5.41,5.42,6.19 C12.21,47.87,34,48,34,48s21.79-0.13,27.1-1.55c2.93-0.78,4.64-3.26,5.42-6.19C67.94,34.95,68,24,68,24S67.94,13.05,66.52,7.74z" fill="#f00"></path>
                                    <path d="M 45,24 27,14 27,34" fill="#fff"></path>
                                </svg>
                            </div>
                        </a>
                    </div>
                `);
                
                // Auto-fill the YouTube ID field
                $('#id_youtube_id').val(videoId);
            } else {
                previewContainer.empty();
                $('#id_youtube_id').val('');
            }
        });
        
        // Trigger preview if URL already exists
        if (youtubeUrlField.val()) {
            youtubeUrlField.trigger('input');
        }
        
        // Add a button to generate a random secret code
        const secretCodeField = $('#id_secret_code');
        const generateButton = $('<button type="button" class="button" id="generate-secret-code" style="margin-left: 10px;">توليد كود عشوائي</button>');
        
        secretCodeField.after(generateButton);
        
        generateButton.on('click', function(e) {
            e.preventDefault();
            
            // Generate a random 6-digit code
            const randomCode = Math.floor(100000 + Math.random() * 900000).toString();
            secretCodeField.val(randomCode);
        });
    });
})(django.jQuery);

# Personal Fedora Kinoite Overlay (BlueBuild Template)

## Installation

To rebase an existing atomic Fedora installation to the latest build:

- First rebase to the unsigned image, to get the proper signing keys and policies installed:
  ```
  rpm-ostree rebase ostree-unverified-registry:$REGISTRY_IMAGE:latest
  ```
- Reboot to complete the rebase:
  ```
  systemctl reboot
  ```
- Then rebase to the signed image, like so:
  ```
  rpm-ostree rebase ostree-image-signed:docker://$REGISTRY_IMAGE:latest
  ```
- Reboot again to complete the installation
  ```
  systemctl reboot
  ```

The `latest` tag will automatically point to the latest build. That build will still always use the Fedora version specified in `recipe.yml`, so you won't get accidentally updated to the next major version.

## Verification

These images are signed with [Sigstore](https://www.sigstore.dev/)'s [cosign](https://github.com/sigstore/cosign). You can verify the signature by downloading the `cosign.pub` file from this repo and running the following command:

```bash
cosign verify --key cosign.pub $REGISTRY_IMAGE
```

## Resources

* [BlueBuild CLI](https://github.com/blue-build/cli)
* [BlueBuild Template](https://github.com/blue-build/template)
* [Fedora Kinoite](https://docs.fedoraproject.org/en-US/fedora-kinoite/)
* [RPM Fusion](https://rpmfusion.org/)
* [Boot OSTree Deployments with UEFI Secure Boot and TPM secrets](https://github.com/prydom/finalize-ostree-uki)
- [1Password LD_PRELOAD inotify Workaround - inotify_add_watch](https://github.com/prydom/1password-ldpreload-inotify)

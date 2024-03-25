# Personal Fedora Kinoite Overlay (BlueBuild Template)


## Build

This repo uses BlueBuild to generate a Containerfile (Dockerfile) from yaml recipes.
Install BlueBuild and its dependencies using instructions from [BlueBuild CLI](https://github.com/blue-build/cli).

Use `bluebuild template -o Containerfile config/fedora-kinoite-laptop.yml` to generate the Containerfile and inspect what will be built.

Use `bluebuild build config/fedora-kinoite-laptop.yml` or `podman build --format docker --pull -t oci-archive:./fedora-kinoite-laptop.tar .` to locally build the image. Note that the former command will save the image to your local container manager storage, while the latter command will save the container to a tar file. If you are building with a rootless container manager, it is recommended you use the second method.

The image will not be signed with these methods. Sigstore is only applicable to images pushed to a registry.

## Installation

Due to a few of the packages having proprietary licenses, I am keeping the container images private.
To configure private container registries use the `/etc/ostree/auth.json` file.

To rebase an existing atomic Fedora installation to the latest build:

- For this image you should first bootstrap [Boot OSTree Deployments with UEFI Secure Boot and TPM secrets](https://github.com/prydom/finalize-ostree-uki) although I don't think it will be un-bootable without.
- Determine what `$REGISTRY_IMAGE` should be. It is the address of the image in the [containers-transports(5)](https://github.com/containers/image/blob/main/docs/containers-transports.5.md) syntax.
- First rebase to the unsigned image, to get the proper signing keys and policies installed:
  ```
  rpm-ostree rebase ostree-unverified-registry:$REGISTRY_IMAGE:latest
  // or to rebase to a local build
  sudo cp ./fedora-kinoite-laptop.tar /var/local/
  rpm-ostree rebase "ostree-unverified-image:oci-archive:/var/local/fedora-kinoite-laptop.tar"
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

The `latest` tag will automatically point to the latest build. That build will still always use the Fedora version specified in the recipe yaml, so you won't get accidentally updated to the next major version.

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
* [1Password LD_PRELOAD inotify Workaround - inotify_add_watch](https://github.com/prydom/1password-ldpreload-inotify)
